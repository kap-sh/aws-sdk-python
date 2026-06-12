from typing import Optional, TYPE_CHECKING
from aws_sdk_workspaces_web._services.async_work_spaces_web import ensure_async_iterator
from aws_sdk_workspaces_web._services.work_spaces_web import ensure_sync_iterator
from aws_sdk_workspaces_web._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_workspaces_web._auth._signers
import aws_sdk_workspaces_web._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_workspaces_web._services.work_spaces_web import WorkSpacesWebClient, WorkSpacesWebClientConfig
    from aws_sdk_workspaces_web._services.async_work_spaces_web import AsyncWorkSpacesWebClient, AsyncWorkSpacesWebClientConfig
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.branding_configuration_create_input
    import aws_sdk_workspaces_web.types.branding_configuration_update_input
    import aws_sdk_workspaces_web.types.client_token
    import aws_sdk_workspaces_web.types.cookie_synchronization_configuration
    import aws_sdk_workspaces_web.types.create_user_settings_request
    import aws_sdk_workspaces_web.types.create_user_settings_response
    import aws_sdk_workspaces_web.types.delete_user_settings_request
    import aws_sdk_workspaces_web.types.delete_user_settings_response
    import aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes
    import aws_sdk_workspaces_web.types.enabled_type
    import aws_sdk_workspaces_web.types.encryption_context_map
    import aws_sdk_workspaces_web.types.get_user_settings_request
    import aws_sdk_workspaces_web.types.get_user_settings_response
    import aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes
    import aws_sdk_workspaces_web.types.key_arn
    import aws_sdk_workspaces_web.types.list_user_settings_request
    import aws_sdk_workspaces_web.types.list_user_settings_response
    import aws_sdk_workspaces_web.types.max_results
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.tag_list
    import aws_sdk_workspaces_web.types.toolbar_configuration
    import aws_sdk_workspaces_web.types.update_user_settings_request
    import aws_sdk_workspaces_web.types.update_user_settings_response

class UserSettingsResource:
    def __init__(self, service: WorkSpacesWebClient) -> None:
        self._service = service
    def create(self, copy_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", paste_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", download_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", upload_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", print_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None, tags: Optional["aws_sdk_workspaces_web.types.tag_list.TagList"] = None, disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"] = None, idle_disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None, cookie_synchronization_configuration: Optional["aws_sdk_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"] = None, customer_managed_key: Optional["aws_sdk_workspaces_web.types.key_arn.keyArn"] = None, additional_encryption_context: Optional["aws_sdk_workspaces_web.types.encryption_context_map.EncryptionContextMap"] = None, deep_link_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, toolbar_configuration: Optional["aws_sdk_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"] = None, branding_configuration_input: Optional["aws_sdk_workspaces_web.types.branding_configuration_create_input.BrandingConfigurationCreateInput"] = None, web_authn_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None) -> "aws_sdk_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse":
        """<p>Creates a user settings resource that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices. </p>

        Args:
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            tags: <p>The tags to add to the user settings resource. A tag is a key-value pair.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p>
            customer_managed_key: <p>The customer managed key used to encrypt sensitive information in the user settings.</p>
            additional_encryption_context: <p>The additional encryption context of the user settings.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration input that customizes the appearance of the web portal for end users. This includes a custom logo, favicon, localized strings, color theme, and optionally a wallpaper and terms of service.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings.create_user_settings(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["copy_allowed"] = copy_allowed
        input["paste_allowed"] = paste_allowed
        input["download_allowed"] = download_allowed
        input["upload_allowed"] = upload_allowed
        input["print_allowed"] = print_allowed
        if tags is not None:
            input["tags"] = tags
        if disconnect_timeout_in_minutes is not None:
            input["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input["idle_disconnect_timeout_in_minutes"] = idle_disconnect_timeout_in_minutes
        if client_token is not None:
            input["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input["cookie_synchronization_configuration"] = cookie_synchronization_configuration
        if customer_managed_key is not None:
            input["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input["additional_encryption_context"] = additional_encryption_context
        if deep_link_allowed is not None:
            input["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input["web_authn_allowed"] = web_authn_allowed

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse":
        """<p>Gets user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings.get_user_settings(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["user_settings_arn"] = user_settings_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None, copy_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, paste_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, download_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, upload_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, print_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"] = None, idle_disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None, cookie_synchronization_configuration: Optional["aws_sdk_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"] = None, deep_link_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, toolbar_configuration: Optional["aws_sdk_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"] = None, branding_configuration_input: Optional["aws_sdk_workspaces_web.types.branding_configuration_update_input.BrandingConfigurationUpdateInput"] = None, web_authn_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None) -> "aws_sdk_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse":
        """<p>Updates the user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p> <p>If the allowlist and blocklist are empty, the configuration becomes null.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration that customizes the appearance of the web portal for end users. When updating user settings without an existing branding configuration, all fields (logo, favicon, localized strings, and color theme) are required except for wallpaper and terms of service. When updating user settings with an existing branding configuration, all fields are optional.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings.update_user_settings(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["user_settings_arn"] = user_settings_arn
        if copy_allowed is not None:
            input["copy_allowed"] = copy_allowed
        if paste_allowed is not None:
            input["paste_allowed"] = paste_allowed
        if download_allowed is not None:
            input["download_allowed"] = download_allowed
        if upload_allowed is not None:
            input["upload_allowed"] = upload_allowed
        if print_allowed is not None:
            input["print_allowed"] = print_allowed
        if disconnect_timeout_in_minutes is not None:
            input["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input["idle_disconnect_timeout_in_minutes"] = idle_disconnect_timeout_in_minutes
        if client_token is not None:
            input["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input["cookie_synchronization_configuration"] = cookie_synchronization_configuration
        if deep_link_allowed is not None:
            input["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input["web_authn_allowed"] = web_authn_allowed

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[WorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse":
        """<p>Deletes user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings.delete_user_settings(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["user_settings_arn"] = user_settings_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[WorkSpacesWebClientConfig] = None, next_token: Optional["aws_sdk_workspaces_web.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_workspaces_web.types.max_results.MaxResults"] = None) -> "aws_sdk_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse":
        """<p>Retrieves a list of user settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation. </p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest]') -> OperationResponse["aws_sdk_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings
            output, http_response = aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings.list_user_settings(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncUserSettingsResource:
    def __init__(self, service: AsyncWorkSpacesWebClient) -> None:
        self._service = service
    async def create(self, copy_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", paste_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", download_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", upload_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", print_allowed: "aws_sdk_workspaces_web.types.enabled_type.EnabledType", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, tags: Optional["aws_sdk_workspaces_web.types.tag_list.TagList"] = None, disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"] = None, idle_disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None, cookie_synchronization_configuration: Optional["aws_sdk_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"] = None, customer_managed_key: Optional["aws_sdk_workspaces_web.types.key_arn.keyArn"] = None, additional_encryption_context: Optional["aws_sdk_workspaces_web.types.encryption_context_map.EncryptionContextMap"] = None, deep_link_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, toolbar_configuration: Optional["aws_sdk_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"] = None, branding_configuration_input: Optional["aws_sdk_workspaces_web.types.branding_configuration_create_input.BrandingConfigurationCreateInput"] = None, web_authn_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None) -> "aws_sdk_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse":
        """<p>Creates a user settings resource that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices. </p>

        Args:
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            tags: <p>The tags to add to the user settings resource. A tag is a key-value pair.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p>
            customer_managed_key: <p>The customer managed key used to encrypt sensitive information in the user settings.</p>
            additional_encryption_context: <p>The additional encryption context of the user settings.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration input that customizes the appearance of the web portal for end users. This includes a custom logo, favicon, localized strings, color theme, and optionally a wallpaper and terms of service.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings.async_create_user_settings(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["copy_allowed"] = copy_allowed
        input["paste_allowed"] = paste_allowed
        input["download_allowed"] = download_allowed
        input["upload_allowed"] = upload_allowed
        input["print_allowed"] = print_allowed
        if tags is not None:
            input["tags"] = tags
        if disconnect_timeout_in_minutes is not None:
            input["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input["idle_disconnect_timeout_in_minutes"] = idle_disconnect_timeout_in_minutes
        if client_token is not None:
            input["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input["cookie_synchronization_configuration"] = cookie_synchronization_configuration
        if customer_managed_key is not None:
            input["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input["additional_encryption_context"] = additional_encryption_context
        if deep_link_allowed is not None:
            input["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input["web_authn_allowed"] = web_authn_allowed

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse":
        """<p>Gets user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings.async_get_user_settings(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["user_settings_arn"] = user_settings_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, copy_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, paste_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, download_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, upload_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, print_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"] = None, idle_disconnect_timeout_in_minutes: Optional["aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"] = None, client_token: Optional["aws_sdk_workspaces_web.types.client_token.ClientToken"] = None, cookie_synchronization_configuration: Optional["aws_sdk_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"] = None, deep_link_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None, toolbar_configuration: Optional["aws_sdk_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"] = None, branding_configuration_input: Optional["aws_sdk_workspaces_web.types.branding_configuration_update_input.BrandingConfigurationUpdateInput"] = None, web_authn_allowed: Optional["aws_sdk_workspaces_web.types.enabled_type.EnabledType"] = None) -> "aws_sdk_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse":
        """<p>Updates the user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p> <p>If the allowlist and blocklist are empty, the configuration becomes null.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration that customizes the appearance of the web portal for end users. When updating user settings without an existing branding configuration, all fields (logo, favicon, localized strings, and color theme) are required except for wallpaper and terms of service. When updating user settings with an existing branding configuration, all fields are optional.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings.async_update_user_settings(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["user_settings_arn"] = user_settings_arn
        if copy_allowed is not None:
            input["copy_allowed"] = copy_allowed
        if paste_allowed is not None:
            input["paste_allowed"] = paste_allowed
        if download_allowed is not None:
            input["download_allowed"] = download_allowed
        if upload_allowed is not None:
            input["upload_allowed"] = upload_allowed
        if print_allowed is not None:
            input["print_allowed"] = print_allowed
        if disconnect_timeout_in_minutes is not None:
            input["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input["idle_disconnect_timeout_in_minutes"] = idle_disconnect_timeout_in_minutes
        if client_token is not None:
            input["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input["cookie_synchronization_configuration"] = cookie_synchronization_configuration
        if deep_link_allowed is not None:
            input["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input["web_authn_allowed"] = web_authn_allowed

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN", *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None) -> "aws_sdk_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse":
        """<p>Deletes user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings.async_delete_user_settings(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest = {}  # type: ignore[typeddict-item]
        input["user_settings_arn"] = user_settings_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None, next_token: Optional["aws_sdk_workspaces_web.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_workspaces_web.types.max_results.MaxResults"] = None) -> "aws_sdk_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse":
        """<p>Retrieves a list of user settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation. </p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest]') -> AsyncOperationResponse["aws_sdk_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse"]:
            import aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings
            output, http_response = await aws_sdk_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings.async_list_user_settings(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output