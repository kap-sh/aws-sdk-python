from typing import TYPE_CHECKING, Optional

from aws_sdk_sso_admin._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.delete_application_grant_request
    import aws_sdk_sso_admin.types.get_application_grant_request
    import aws_sdk_sso_admin.types.get_application_grant_response
    import aws_sdk_sso_admin.types.grant
    import aws_sdk_sso_admin.types.grant_item
    import aws_sdk_sso_admin.types.grant_type
    import aws_sdk_sso_admin.types.list_application_grants_request
    import aws_sdk_sso_admin.types.list_application_grants_response
    import aws_sdk_sso_admin.types.put_application_grant_request
    import aws_sdk_sso_admin.types.token
    from aws_sdk_sso_admin._services.async_sso_admin import (
        AsyncSSOAdminClient,
        AsyncSSOAdminClientConfig,
    )
    from aws_sdk_sso_admin._services.sso_admin import (
        SSOAdminClient,
        SSOAdminClientConfig,
    )


class ApplicationGrantResource:
    def __init__(self, service: SSOAdminClient) -> None:
        self._service = service

    def put(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType",
        grant: "aws_sdk_sso_admin.types.grant.Grant",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Creates a configuration for an application to use grants. Conceptually grants are authorization to request actions related to tokens. This configuration will be used when parties are requesting and receiving tokens during the trusted identity propagation process. For more information on the IAM Identity Center supported grant workflows, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html\">SAML 2.0 and OAuth 2.0</a>.</p> <p>A grant is created between your applications and Identity Center instance which enables an application to use specified mechanisms to obtain tokens. These tokens are used by your applications to gain access to Amazon Web Services resources on behalf of users. The following elements are within these exchanges:</p> <ul> <li> <p> <b>Requester</b> - The application requesting access to Amazon Web Services resources.</p> </li> <li> <p> <b>Subject</b> - Typically the user that is requesting access to Amazon Web Services resources.</p> </li> <li> <p> <b>Grant</b> - Conceptually, a grant is authorization to access Amazon Web Services resources. These grants authorize token generation for authenticating access to the requester and for the request to make requests on behalf of the subjects. There are four types of grants:</p> <ul> <li> <p> <b>AuthorizationCode</b> - Allows an application to request authorization through a series of user-agent redirects.</p> </li> <li> <p> <b>JWT bearer </b> - Authorizes an application to exchange a JSON Web Token that came from an external identity provider. To learn more, see <a href=\"https://datatracker.ietf.org/doc/html/rfc6749\">RFC 6479</a>.</p> </li> <li> <p> <b>Refresh token</b> - Enables application to request new access tokens to replace expiring or expired access tokens.</p> </li> <li> <p> <b>Exchange token</b> - A grant that requests tokens from the authorization server by providing a ‘subject’ token with access scope authorizing trusted identity propagation to this application. To learn more, see <a href=\"https://datatracker.ietf.org/doc/html/rfc8693\">RFC 8693</a>.</p> </li> </ul> </li> <li> <p> <b>Authorization server</b> - IAM Identity Center requests tokens.</p> </li> </ul> <p>User credentials are never shared directly within these exchanges. Instead, applications use grants to request access tokens from IAM Identity Center. For more information, see <a href=\"https://datatracker.ietf.org/doc/html/rfc6749\">RFC 6479</a>.</p> <p class=\"title\"> <b>Use cases</b> </p> <ul> <li> <p>Connecting to custom applications.</p> </li> <li> <p>Configuring an Amazon Web Services service to make calls to another Amazon Web Services services using JWT tokens.</p> </li> </ul>

        Args:
            application_arn: <p>Specifies the ARN of the application to update.</p>
            grant_type: <p>Specifies the type of grant to update.</p>
            grant: <p>Specifies a structure that describes the grant to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.put_application_grant_request.PutApplicationGrantRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_application_grant

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.put_application_grant.put_application_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.put_application_grant_request.PutApplicationGrantRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        input["grant_type"] = grant_type
        input["grant"] = grant

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_application_grant_response.GetApplicationGrantResponse":
        """<p>Retrieves details about an application grant.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application that contains the grant.</p>
            grant_type: <p>Specifies the type of grant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.get_application_grant_request.GetApplicationGrantRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.get_application_grant_response.GetApplicationGrantResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_application_grant

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.get_application_grant.get_application_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.get_application_grant_request.GetApplicationGrantRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        input["grant_type"] = grant_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes a grant from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the grant to delete.</p>
            grant_type: <p>Specifies the type of grant to delete from the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_application_grant_request.DeleteApplicationGrantRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_application_grant

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_application_grant.delete_application_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.delete_application_grant_request.DeleteApplicationGrantRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        input["grant_type"] = grant_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_grants_response.ListApplicationGrantsResponse":
        """<p>List the grants associated with an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application whose grants you want to list.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_application_grants_request.ListApplicationGrantsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_application_grants_response.ListApplicationGrantsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_grants

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_application_grants.list_application_grants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.list_application_grants_request.ListApplicationGrantsRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncApplicationGrantResource:
    def __init__(self, service: AsyncSSOAdminClient) -> None:
        self._service = service

    async def put(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType",
        grant: "aws_sdk_sso_admin.types.grant.Grant",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Creates a configuration for an application to use grants. Conceptually grants are authorization to request actions related to tokens. This configuration will be used when parties are requesting and receiving tokens during the trusted identity propagation process. For more information on the IAM Identity Center supported grant workflows, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html\">SAML 2.0 and OAuth 2.0</a>.</p> <p>A grant is created between your applications and Identity Center instance which enables an application to use specified mechanisms to obtain tokens. These tokens are used by your applications to gain access to Amazon Web Services resources on behalf of users. The following elements are within these exchanges:</p> <ul> <li> <p> <b>Requester</b> - The application requesting access to Amazon Web Services resources.</p> </li> <li> <p> <b>Subject</b> - Typically the user that is requesting access to Amazon Web Services resources.</p> </li> <li> <p> <b>Grant</b> - Conceptually, a grant is authorization to access Amazon Web Services resources. These grants authorize token generation for authenticating access to the requester and for the request to make requests on behalf of the subjects. There are four types of grants:</p> <ul> <li> <p> <b>AuthorizationCode</b> - Allows an application to request authorization through a series of user-agent redirects.</p> </li> <li> <p> <b>JWT bearer </b> - Authorizes an application to exchange a JSON Web Token that came from an external identity provider. To learn more, see <a href=\"https://datatracker.ietf.org/doc/html/rfc6749\">RFC 6479</a>.</p> </li> <li> <p> <b>Refresh token</b> - Enables application to request new access tokens to replace expiring or expired access tokens.</p> </li> <li> <p> <b>Exchange token</b> - A grant that requests tokens from the authorization server by providing a ‘subject’ token with access scope authorizing trusted identity propagation to this application. To learn more, see <a href=\"https://datatracker.ietf.org/doc/html/rfc8693\">RFC 8693</a>.</p> </li> </ul> </li> <li> <p> <b>Authorization server</b> - IAM Identity Center requests tokens.</p> </li> </ul> <p>User credentials are never shared directly within these exchanges. Instead, applications use grants to request access tokens from IAM Identity Center. For more information, see <a href=\"https://datatracker.ietf.org/doc/html/rfc6749\">RFC 6479</a>.</p> <p class=\"title\"> <b>Use cases</b> </p> <ul> <li> <p>Connecting to custom applications.</p> </li> <li> <p>Configuring an Amazon Web Services service to make calls to another Amazon Web Services services using JWT tokens.</p> </li> </ul>

        Args:
            application_arn: <p>Specifies the ARN of the application to update.</p>
            grant_type: <p>Specifies the type of grant to update.</p>
            grant: <p>Specifies a structure that describes the grant to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.put_application_grant_request.PutApplicationGrantRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_application_grant

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.put_application_grant.async_put_application_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.put_application_grant_request.PutApplicationGrantRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        input["grant_type"] = grant_type
        input["grant"] = grant

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_application_grant_response.GetApplicationGrantResponse":
        """<p>Retrieves details about an application grant.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application that contains the grant.</p>
            grant_type: <p>Specifies the type of grant.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.get_application_grant_request.GetApplicationGrantRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sso_admin.types.get_application_grant_response.GetApplicationGrantResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_application_grant

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.get_application_grant.async_get_application_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.get_application_grant_request.GetApplicationGrantRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        input["grant_type"] = grant_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        grant_type: "aws_sdk_sso_admin.types.grant_type.GrantType",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes a grant from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the grant to delete.</p>
            grant_type: <p>Specifies the type of grant to delete from the application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.delete_application_grant_request.DeleteApplicationGrantRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_application_grant

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.delete_application_grant.async_delete_application_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.delete_application_grant_request.DeleteApplicationGrantRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        input["grant_type"] = grant_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_grants_response.ListApplicationGrantsResponse":
        """<p>List the grants associated with an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application whose grants you want to list.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.list_application_grants_request.ListApplicationGrantsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sso_admin.types.list_application_grants_response.ListApplicationGrantsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_grants

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.list_application_grants.async_list_application_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sso_admin.types.list_application_grants_request.ListApplicationGrantsRequest = {}  # type: ignore[typeddict-item]
        input["application_arn"] = application_arn
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
