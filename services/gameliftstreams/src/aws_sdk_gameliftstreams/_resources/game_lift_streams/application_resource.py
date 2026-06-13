from typing import TYPE_CHECKING, Optional

import aws_sdk_gameliftstreams._auth._signers
import aws_sdk_gameliftstreams._auth._sigv4
from aws_sdk_gameliftstreams._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.application_log_output_uri
    import aws_sdk_gameliftstreams.types.application_source_uri
    import aws_sdk_gameliftstreams.types.application_summary
    import aws_sdk_gameliftstreams.types.client_token
    import aws_sdk_gameliftstreams.types.create_application_input
    import aws_sdk_gameliftstreams.types.create_application_output
    import aws_sdk_gameliftstreams.types.delete_application_input
    import aws_sdk_gameliftstreams.types.description
    import aws_sdk_gameliftstreams.types.executable_path
    import aws_sdk_gameliftstreams.types.file_paths
    import aws_sdk_gameliftstreams.types.get_application_input
    import aws_sdk_gameliftstreams.types.get_application_output
    import aws_sdk_gameliftstreams.types.identifier
    import aws_sdk_gameliftstreams.types.list_applications_input
    import aws_sdk_gameliftstreams.types.list_applications_output
    import aws_sdk_gameliftstreams.types.max_results
    import aws_sdk_gameliftstreams.types.next_token
    import aws_sdk_gameliftstreams.types.runtime_environment
    import aws_sdk_gameliftstreams.types.tags
    import aws_sdk_gameliftstreams.types.update_application_input
    import aws_sdk_gameliftstreams.types.update_application_output
    from aws_sdk_gameliftstreams._services.async_game_lift_streams import (
        AsyncGameLiftStreamsClient,
        AsyncGameLiftStreamsClientConfig,
    )
    from aws_sdk_gameliftstreams._services.game_lift_streams import (
        GameLiftStreamsClient,
        GameLiftStreamsClientConfig,
    )


class ApplicationResource:
    def __init__(self, service: GameLiftStreamsClient) -> None:
        self._service = service

    def create(
        self,
        description: "aws_sdk_gameliftstreams.types.description.Description",
        runtime_environment: "aws_sdk_gameliftstreams.types.runtime_environment.RuntimeEnvironment",
        executable_path: "aws_sdk_gameliftstreams.types.executable_path.ExecutablePath",
        application_source_uri: "aws_sdk_gameliftstreams.types.application_source_uri.ApplicationSourceUri",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
        application_log_paths: Optional[
            "aws_sdk_gameliftstreams.types.file_paths.FilePaths"
        ] = None,
        application_log_output_uri: Optional[
            "aws_sdk_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
        ] = None,
        tags: Optional["aws_sdk_gameliftstreams.types.tags.Tags"] = None,
        client_token: Optional[
            "aws_sdk_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_gameliftstreams.types.create_application_output.CreateApplicationOutput":
        """<p>Creates an application resource in Amazon GameLift Streams, which specifies the application content you want to stream, such as a game build or other software, and configures the settings to run it.</p> <p> Before you create an application, upload your application content files to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see <b>Getting Started</b> in the Amazon GameLift Streams Developer Guide. </p> <important> <p> Make sure that your files in the Amazon S3 bucket are the correct version you want to use. If you change the files at a later time, you will need to create a new Amazon GameLift Streams application. </p> </important> <p> If the request is successful, Amazon GameLift Streams begins to create an application and sets the status to <code>INITIALIZED</code>. When an application reaches <code>READY</code> status, you can use the application to set up stream groups and start streams. To track application status, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html\">GetApplication</a>. </p>

        Args:
            description: <p>A human-readable label for the application. You can update this value later.</p>
            runtime_environment: <p>Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.</p> <p>A runtime environment can be one of the following:</p> <ul> <li> <p> For Linux applications </p> <ul> <li> <p> Ubuntu 22.04 LTS (<code>Type=UBUNTU, Version=22_04_LTS</code>) </p> </li> </ul> </li> <li> <p> For Windows applications </p> <ul> <li> <p>Microsoft Windows Server 2022 Base (<code>Type=WINDOWS, Version=2022</code>)</p> </li> <li> <p>Proton 10.0-4 (<code>Type=PROTON, Version=20260204</code>)</p> </li> <li> <p>Proton 9.0-2 (<code>Type=PROTON, Version=20250516</code>)</p> </li> <li> <p>Proton 8.0-5 (<code>Type=PROTON, Version=20241007</code>)</p> </li> <li> <p>Proton 8.0-2c (<code>Type=PROTON, Version=20230704</code>)</p> </li> </ul> </li> </ul>
            executable_path: <p>The relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the location set in <code>ApplicationSourceUri</code>. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('<code>#!</code>').</p>
            application_source_uri: <p>The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.</p> <p>This value is immutable. To designate a different content location, create a new application.</p> <note> <p>The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same Amazon Web Services Region.</p> </note>
            application_log_paths: <p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>
            application_log_output_uri: <p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template\">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> </note>
            tags: <p>A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html\">TagResource</a> to add tags, <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html\">UntagResource</a> to remove tags, and <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html\">ListTagsForResource</a> to view tags on existing resources.</p>
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_gameliftstreams.types.create_application_input.CreateApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_gameliftstreams.types.create_application_output.CreateApplicationOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.create_application

            output, http_response = (
                aws_sdk_gameliftstreams._operations.game_lift_streams.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.create_application_input.CreateApplicationInput = {}  # type: ignore[typeddict-item]
        input["description"] = description
        input["runtime_environment"] = runtime_environment
        input["executable_path"] = executable_path
        input["application_source_uri"] = application_source_uri
        if application_log_paths is not None:
            input["application_log_paths"] = application_log_paths
        if application_log_output_uri is not None:
            input["application_log_output_uri"] = application_log_output_uri
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
    ) -> "aws_sdk_gameliftstreams.types.get_application_output.GetApplicationOutput":
        """<p>Retrieves properties for an Amazon GameLift Streams application resource. Specify the ID of the application that you want to retrieve. If the operation is successful, it returns properties for the requested application.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_gameliftstreams.types.get_application_input.GetApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_gameliftstreams.types.get_application_output.GetApplicationOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.get_application

            output, http_response = (
                aws_sdk_gameliftstreams._operations.game_lift_streams.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.get_application_input.GetApplicationInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
        description: Optional[
            "aws_sdk_gameliftstreams.types.description.Description"
        ] = None,
        application_log_paths: Optional[
            "aws_sdk_gameliftstreams.types.file_paths.FilePaths"
        ] = None,
        application_log_output_uri: Optional[
            "aws_sdk_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
        ] = None,
    ) -> "aws_sdk_gameliftstreams.types.update_application_output.UpdateApplicationOutput":
        """<p> Updates the mutable configuration settings for a Amazon GameLift Streams application resource. You can change the <code>Description</code>, <code>ApplicationLogOutputUri</code>, and <code>ApplicationLogPaths</code>. </p> <p>To update application settings, specify the application ID and provide the new values. If the operation is successful, it returns the complete updated set of settings for the application.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            description: <p>A human-readable label for the application.</p>
            application_log_paths: <p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>
            application_log_output_uri: <p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template\">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_gameliftstreams.types.update_application_input.UpdateApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_gameliftstreams.types.update_application_output.UpdateApplicationOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.update_application

            output, http_response = (
                aws_sdk_gameliftstreams._operations.game_lift_streams.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.update_application_input.UpdateApplicationInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if description is not None:
            input["description"] = description
        if application_log_paths is not None:
            input["application_log_paths"] = application_log_paths
        if application_log_output_uri is not None:
            input["application_log_output_uri"] = application_log_output_uri

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
    ) -> None:
        """<p>Permanently deletes an Amazon GameLift Streams application resource. This also deletes the application content files stored with Amazon GameLift Streams. However, this does not delete the original files that you uploaded to your Amazon S3 bucket; you can delete these any time after Amazon GameLift Streams creates an application, which is the only time Amazon GameLift Streams accesses your Amazon S3 bucket.</p> <p> You can only delete an application that meets the following conditions: </p> <ul> <li> <p>The application is in <code>READY</code> or <code>ERROR</code> status. You cannot delete an application that's in <code>PROCESSING</code> or <code>INITIALIZED</code> status.</p> </li> <li> <p>The application is not the default application of any stream groups. You must first delete the stream group by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html\">DeleteStreamGroup</a>.</p> </li> <li> <p>The application is not linked to any stream groups. You must first unlink the stream group by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html\">DisassociateApplications</a>.</p> </li> <li> <p> An application is not streaming in any ongoing stream session. You must wait until the client ends the stream session or call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html\">TerminateStreamSession</a> to end the stream. </p> </li> </ul> <p>If any active stream groups exist for this application, this request returns a <code>ValidationException</code>. </p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_gameliftstreams.types.delete_application_input.DeleteApplicationInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.delete_application

            output, http_response = (
                aws_sdk_gameliftstreams._operations.game_lift_streams.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.delete_application_input.DeleteApplicationInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[GameLiftStreamsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_gameliftstreams.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "aws_sdk_gameliftstreams.types.list_applications_output.ListApplicationsOutput"
    ):
        """<p>Retrieves a list of all Amazon GameLift Streams applications that are associated with the Amazon Web Services account in use. This operation returns applications in all statuses, in no particular order. You can paginate the results as needed.</p>

        Args:
            next_token: <p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_gameliftstreams.types.list_applications_input.ListApplicationsInput]",
        ) -> OperationResponse[
            "aws_sdk_gameliftstreams.types.list_applications_output.ListApplicationsOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.list_applications

            output, http_response = (
                aws_sdk_gameliftstreams._operations.game_lift_streams.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.list_applications_input.ListApplicationsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncApplicationResource:
    def __init__(self, service: AsyncGameLiftStreamsClient) -> None:
        self._service = service

    async def create(
        self,
        description: "aws_sdk_gameliftstreams.types.description.Description",
        runtime_environment: "aws_sdk_gameliftstreams.types.runtime_environment.RuntimeEnvironment",
        executable_path: "aws_sdk_gameliftstreams.types.executable_path.ExecutablePath",
        application_source_uri: "aws_sdk_gameliftstreams.types.application_source_uri.ApplicationSourceUri",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        application_log_paths: Optional[
            "aws_sdk_gameliftstreams.types.file_paths.FilePaths"
        ] = None,
        application_log_output_uri: Optional[
            "aws_sdk_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
        ] = None,
        tags: Optional["aws_sdk_gameliftstreams.types.tags.Tags"] = None,
        client_token: Optional[
            "aws_sdk_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_gameliftstreams.types.create_application_output.CreateApplicationOutput":
        """<p>Creates an application resource in Amazon GameLift Streams, which specifies the application content you want to stream, such as a game build or other software, and configures the settings to run it.</p> <p> Before you create an application, upload your application content files to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see <b>Getting Started</b> in the Amazon GameLift Streams Developer Guide. </p> <important> <p> Make sure that your files in the Amazon S3 bucket are the correct version you want to use. If you change the files at a later time, you will need to create a new Amazon GameLift Streams application. </p> </important> <p> If the request is successful, Amazon GameLift Streams begins to create an application and sets the status to <code>INITIALIZED</code>. When an application reaches <code>READY</code> status, you can use the application to set up stream groups and start streams. To track application status, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html\">GetApplication</a>. </p>

        Args:
            description: <p>A human-readable label for the application. You can update this value later.</p>
            runtime_environment: <p>Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.</p> <p>A runtime environment can be one of the following:</p> <ul> <li> <p> For Linux applications </p> <ul> <li> <p> Ubuntu 22.04 LTS (<code>Type=UBUNTU, Version=22_04_LTS</code>) </p> </li> </ul> </li> <li> <p> For Windows applications </p> <ul> <li> <p>Microsoft Windows Server 2022 Base (<code>Type=WINDOWS, Version=2022</code>)</p> </li> <li> <p>Proton 10.0-4 (<code>Type=PROTON, Version=20260204</code>)</p> </li> <li> <p>Proton 9.0-2 (<code>Type=PROTON, Version=20250516</code>)</p> </li> <li> <p>Proton 8.0-5 (<code>Type=PROTON, Version=20241007</code>)</p> </li> <li> <p>Proton 8.0-2c (<code>Type=PROTON, Version=20230704</code>)</p> </li> </ul> </li> </ul>
            executable_path: <p>The relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the location set in <code>ApplicationSourceUri</code>. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('<code>#!</code>').</p>
            application_source_uri: <p>The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.</p> <p>This value is immutable. To designate a different content location, create a new application.</p> <note> <p>The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same Amazon Web Services Region.</p> </note>
            application_log_paths: <p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>
            application_log_output_uri: <p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template\">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> </note>
            tags: <p>A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html\">TagResource</a> to add tags, <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html\">UntagResource</a> to remove tags, and <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html\">ListTagsForResource</a> to view tags on existing resources.</p>
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_gameliftstreams.types.create_application_input.CreateApplicationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_gameliftstreams.types.create_application_output.CreateApplicationOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.create_application

            (
                output,
                http_response,
            ) = await aws_sdk_gameliftstreams._operations.game_lift_streams.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.create_application_input.CreateApplicationInput = {}  # type: ignore[typeddict-item]
        input["description"] = description
        input["runtime_environment"] = runtime_environment
        input["executable_path"] = executable_path
        input["application_source_uri"] = application_source_uri
        if application_log_paths is not None:
            input["application_log_paths"] = application_log_paths
        if application_log_output_uri is not None:
            input["application_log_output_uri"] = application_log_output_uri
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "aws_sdk_gameliftstreams.types.get_application_output.GetApplicationOutput":
        """<p>Retrieves properties for an Amazon GameLift Streams application resource. Specify the ID of the application that you want to retrieve. If the operation is successful, it returns properties for the requested application.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_gameliftstreams.types.get_application_input.GetApplicationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_gameliftstreams.types.get_application_output.GetApplicationOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.get_application

            (
                output,
                http_response,
            ) = await aws_sdk_gameliftstreams._operations.game_lift_streams.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.get_application_input.GetApplicationInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        description: Optional[
            "aws_sdk_gameliftstreams.types.description.Description"
        ] = None,
        application_log_paths: Optional[
            "aws_sdk_gameliftstreams.types.file_paths.FilePaths"
        ] = None,
        application_log_output_uri: Optional[
            "aws_sdk_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
        ] = None,
    ) -> "aws_sdk_gameliftstreams.types.update_application_output.UpdateApplicationOutput":
        """<p> Updates the mutable configuration settings for a Amazon GameLift Streams application resource. You can change the <code>Description</code>, <code>ApplicationLogOutputUri</code>, and <code>ApplicationLogPaths</code>. </p> <p>To update application settings, specify the application ID and provide the new values. If the operation is successful, it returns the complete updated set of settings for the application.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            description: <p>A human-readable label for the application.</p>
            application_log_paths: <p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>
            application_log_output_uri: <p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template\">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_gameliftstreams.types.update_application_input.UpdateApplicationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_gameliftstreams.types.update_application_output.UpdateApplicationOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.update_application

            (
                output,
                http_response,
            ) = await aws_sdk_gameliftstreams._operations.game_lift_streams.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.update_application_input.UpdateApplicationInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if description is not None:
            input["description"] = description
        if application_log_paths is not None:
            input["application_log_paths"] = application_log_paths
        if application_log_output_uri is not None:
            input["application_log_output_uri"] = application_log_output_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> None:
        """<p>Permanently deletes an Amazon GameLift Streams application resource. This also deletes the application content files stored with Amazon GameLift Streams. However, this does not delete the original files that you uploaded to your Amazon S3 bucket; you can delete these any time after Amazon GameLift Streams creates an application, which is the only time Amazon GameLift Streams accesses your Amazon S3 bucket.</p> <p> You can only delete an application that meets the following conditions: </p> <ul> <li> <p>The application is in <code>READY</code> or <code>ERROR</code> status. You cannot delete an application that's in <code>PROCESSING</code> or <code>INITIALIZED</code> status.</p> </li> <li> <p>The application is not the default application of any stream groups. You must first delete the stream group by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html\">DeleteStreamGroup</a>.</p> </li> <li> <p>The application is not linked to any stream groups. You must first unlink the stream group by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html\">DisassociateApplications</a>.</p> </li> <li> <p> An application is not streaming in any ongoing stream session. You must wait until the client ends the stream session or call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html\">TerminateStreamSession</a> to end the stream. </p> </li> </ul> <p>If any active stream groups exist for this application, this request returns a <code>ValidationException</code>. </p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_gameliftstreams.types.delete_application_input.DeleteApplicationInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.delete_application

            (
                output,
                http_response,
            ) = await aws_sdk_gameliftstreams._operations.game_lift_streams.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.delete_application_input.DeleteApplicationInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_gameliftstreams.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "aws_sdk_gameliftstreams.types.list_applications_output.ListApplicationsOutput"
    ):
        """<p>Retrieves a list of all Amazon GameLift Streams applications that are associated with the Amazon Web Services account in use. This operation returns applications in all statuses, in no particular order. You can paginate the results as needed.</p>

        Args:
            next_token: <p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_gameliftstreams.types.list_applications_input.ListApplicationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_gameliftstreams.types.list_applications_output.ListApplicationsOutput"
        ]:
            import aws_sdk_gameliftstreams._operations.game_lift_streams.list_applications

            (
                output,
                http_response,
            ) = await aws_sdk_gameliftstreams._operations.game_lift_streams.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_gameliftstreams.types.list_applications_input.ListApplicationsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
