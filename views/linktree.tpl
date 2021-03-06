<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
    <title>Linktree - {{name}}</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon"/>
</head>

<body>
    <img id="userPhoto" src="me.jpg" alt="User Photo">
        <h1 id="userName">{{name}}</h1>
        % if sname:
        <h2 id="userName">- {{sname}}</h2>
        % end
    <div id="links">
            % if email:
            <a class="link" href="mailto:{{email}}">
            <img id="socialMediaPhoto" src="icons/email-14-128.png" alt="Email icon"></a>
            % end
            % if facebook:
            <a class="link" href="https://www.facebook.com/{{facebook}}" target='_blank noopener'>
            <img id="socialMediaPhoto" src="icons/Facebook_1.png" alt="Facebook icon"></a>
            % end
            % if github:
            <a class="link" href="https://github.com/{{github}}" target='_blank noopener'>
            <img id="socialMediaPhoto" src="icons/Github_1.png" alt="Github icon"></a>
            % end
            % if ig:
            <a class="link" href="https://instagram.com/{{ig}}" target='_blank noopener'>
            <img id="socialMediaPhoto" src="icons/Instagram_1.png" alt="Instagram icon"></a>
            % end
            % if reddit:
            <a class="link" href="https://www.reddit.com/user/{{reddit}}" target='_blank noopener'>
            <img id="socialMediaPhoto" src="icons/Reddit_1.png" alt="Reddit icon"></a>
            % end
            % if twitter:
            <a class="link" href="https://twitter.com/{{twitter}}" target='_blank noopener'>
            <img id="socialMediaPhoto" src="icons/Twitter_1.png" alt="Twitter icon"></a>
            % end
            % if youtube:
            <a class="link" href="https://www.youtube.com/channel/{{youtube}}" target='_blank noopener'>
            <img id="socialMediaPhoto" src="icons/Youtube_1.png" alt="Youtube icon"></a>
            % end
    </div>
</body>

</html>

