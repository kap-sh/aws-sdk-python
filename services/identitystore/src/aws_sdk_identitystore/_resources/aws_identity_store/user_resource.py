from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_identitystore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.addresses
    import aws_sdk_identitystore.types.attribute_operations
    import aws_sdk_identitystore.types.create_user_request
    import aws_sdk_identitystore.types.create_user_response
    import aws_sdk_identitystore.types.delete_user_request
    import aws_sdk_identitystore.types.delete_user_response
    import aws_sdk_identitystore.types.describe_user_request
    import aws_sdk_identitystore.types.describe_user_response
    import aws_sdk_identitystore.types.emails
    import aws_sdk_identitystore.types.extension_names
    import aws_sdk_identitystore.types.extensions
    import aws_sdk_identitystore.types.filters
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.list_users_request
    import aws_sdk_identitystore.types.list_users_response
    import aws_sdk_identitystore.types.max_results
    import aws_sdk_identitystore.types.name
    import aws_sdk_identitystore.types.next_token
    import aws_sdk_identitystore.types.phone_numbers
    import aws_sdk_identitystore.types.photos
    import aws_sdk_identitystore.types.resource_id
    import aws_sdk_identitystore.types.roles
    import aws_sdk_identitystore.types.sensitive_string_type
    import aws_sdk_identitystore.types.update_user_request
    import aws_sdk_identitystore.types.update_user_response
    import aws_sdk_identitystore.types.user
    import aws_sdk_identitystore.types.user_name
    from aws_sdk_identitystore._services.async_identitystore import (
        AsyncidentitystoreClient,
        AsyncidentitystoreClientConfig,
    )
    from aws_sdk_identitystore._services.identitystore import (
        identitystoreClient,
        identitystoreClientConfig,
    )


class UserResource:
    def __init__(self, service: identitystoreClient) -> None:
        self._service = service

    def create(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        user_name: Optional["aws_sdk_identitystore.types.user_name.UserName"] = None,
        name: Optional["aws_sdk_identitystore.types.name.Name"] = None,
        display_name: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        nick_name: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        profile_url: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        emails: Optional["aws_sdk_identitystore.types.emails.Emails"] = None,
        addresses: Optional["aws_sdk_identitystore.types.addresses.Addresses"] = None,
        phone_numbers: Optional[
            "aws_sdk_identitystore.types.phone_numbers.PhoneNumbers"
        ] = None,
        user_type: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        title: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        preferred_language: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        locale: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        timezone: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        photos: Optional["aws_sdk_identitystore.types.photos.Photos"] = None,
        website: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        birthdate: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        roles: Optional["aws_sdk_identitystore.types.roles.Roles"] = None,
        extensions: Optional[
            "aws_sdk_identitystore.types.extensions.Extensions"
        ] = None,
    ) -> "aws_sdk_identitystore.types.create_user_response.CreateUserResponse":
        r"""<p>Creates a user within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_name: <p>A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>
            name: <p>An object containing the name of the user. When used in IAM Identity Center, this parameter is required.</p>
            display_name: <p>A string containing the name of the user. This value is typically formatted for display when the user is referenced. For example, \"John Doe.\" When used in IAM Identity Center, this parameter is required.</p>
            nick_name: <p>A string containing an alternate name for the user.</p>
            profile_url: <p>A string containing a URL that might be associated with the user.</p>
            emails: <p>A list of <code>Email</code> objects containing email addresses associated with the user.</p>
            addresses: <p>A list of <code>Address</code> objects containing addresses associated with the user.</p>
            phone_numbers: <p>A list of <code>PhoneNumber</code> objects containing phone numbers associated with the user.</p>
            user_type: <p>A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.</p>
            title: <p>A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.</p>
            preferred_language: <p>A string containing the preferred language of the user. For example, \"American English\" or \"en-us.\"</p>
            locale: <p>A string containing the geographical region or location of the user.</p>
            timezone: <p>A string containing the time zone of the user.</p>
            photos: <p>A list of photos associated with the user. You can add up to 3 photos per user. Each photo can include a value, type, display name, and primary designation.</p>
            website: <p>The user's personal website or blog URL. This field allows users to provide a link to their personal or professional website.</p>
            birthdate: <p>The user's birthdate in YYYY-MM-DD format. This field supports standard date format for storing personal information.</p>
            roles: <p>A list of <code>Role</code> objects containing roles associated with the user.</p>
            extensions: <p>A map with additional attribute extensions for the user. Each map key corresponds to an extension name, while map values represent extension data in <code>Document</code> type (not supported by Java V1, Go V1 and older versions of the CLI). <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.create_user

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if user_name is not None:
            input_["user_name"] = user_name
        if name is not None:
            input_["name"] = name
        if display_name is not None:
            input_["display_name"] = display_name
        if nick_name is not None:
            input_["nick_name"] = nick_name
        if profile_url is not None:
            input_["profile_url"] = profile_url
        if emails is not None:
            input_["emails"] = emails
        if addresses is not None:
            input_["addresses"] = addresses
        if phone_numbers is not None:
            input_["phone_numbers"] = phone_numbers
        if user_type is not None:
            input_["user_type"] = user_type
        if title is not None:
            input_["title"] = title
        if preferred_language is not None:
            input_["preferred_language"] = preferred_language
        if locale is not None:
            input_["locale"] = locale
        if timezone is not None:
            input_["timezone"] = timezone
        if photos is not None:
            input_["photos"] = photos
        if website is not None:
            input_["website"] = website
        if birthdate is not None:
            input_["birthdate"] = birthdate
        if roles is not None:
            input_["roles"] = roles
        if extensions is not None:
            input_["extensions"] = extensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        extensions: Optional[
            "aws_sdk_identitystore.types.extension_names.ExtensionNames"
        ] = None,
    ) -> "aws_sdk_identitystore.types.describe_user_response.DescribeUserResponse":
        r"""<p>Retrieves the user metadata and attributes from the <code>UserId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            user_id: <p>The identifier for a user in the identity store.</p>
            extensions: <p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.describe_user_request.DescribeUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.describe_user_response.DescribeUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.describe_user

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.describe_user.describe_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.describe_user_request.DescribeUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["user_id"] = user_id
        if extensions is not None:
            input_["extensions"] = extensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        operations: "aws_sdk_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.update_user_response.UpdateUserResponse":
        r"""<p>Updates the specified user metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_id: <p>The identifier for a user in the identity store.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested user. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html\">User</a>.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.update_user

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["user_id"] = user_id
        input_["operations"] = operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user within an identity store given <code>UserId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_id: <p>The identifier for a user in the identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.delete_user_response.DeleteUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.delete_user

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        extensions: Optional[
            "aws_sdk_identitystore.types.extension_names.ExtensionNames"
        ] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_identitystore.types.filters.Filters"] = None,
    ) -> "aws_sdk_identitystore.types.list_users_response.ListUsersResponse":
        r"""<p>Lists all users in the identity store. Returns a paginated list of complete <code>User</code> objects. Filtering for a <code>User</code> by the <code>UserName</code> attribute is deprecated. Instead, use the <code>GetUserId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            extensions: <p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests. </p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.list_users_response.ListUsersResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_users

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_users_request.ListUsersRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if extensions is not None:
            input_["extensions"] = extensions
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncUserResource:
    def __init__(self, service: AsyncidentitystoreClient) -> None:
        self._service = service

    async def create(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        user_name: Optional["aws_sdk_identitystore.types.user_name.UserName"] = None,
        name: Optional["aws_sdk_identitystore.types.name.Name"] = None,
        display_name: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        nick_name: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        profile_url: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        emails: Optional["aws_sdk_identitystore.types.emails.Emails"] = None,
        addresses: Optional["aws_sdk_identitystore.types.addresses.Addresses"] = None,
        phone_numbers: Optional[
            "aws_sdk_identitystore.types.phone_numbers.PhoneNumbers"
        ] = None,
        user_type: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        title: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        preferred_language: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        locale: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        timezone: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        photos: Optional["aws_sdk_identitystore.types.photos.Photos"] = None,
        website: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        birthdate: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
        roles: Optional["aws_sdk_identitystore.types.roles.Roles"] = None,
        extensions: Optional[
            "aws_sdk_identitystore.types.extensions.Extensions"
        ] = None,
    ) -> "aws_sdk_identitystore.types.create_user_response.CreateUserResponse":
        r"""<p>Creates a user within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_name: <p>A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>
            name: <p>An object containing the name of the user. When used in IAM Identity Center, this parameter is required.</p>
            display_name: <p>A string containing the name of the user. This value is typically formatted for display when the user is referenced. For example, \"John Doe.\" When used in IAM Identity Center, this parameter is required.</p>
            nick_name: <p>A string containing an alternate name for the user.</p>
            profile_url: <p>A string containing a URL that might be associated with the user.</p>
            emails: <p>A list of <code>Email</code> objects containing email addresses associated with the user.</p>
            addresses: <p>A list of <code>Address</code> objects containing addresses associated with the user.</p>
            phone_numbers: <p>A list of <code>PhoneNumber</code> objects containing phone numbers associated with the user.</p>
            user_type: <p>A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.</p>
            title: <p>A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.</p>
            preferred_language: <p>A string containing the preferred language of the user. For example, \"American English\" or \"en-us.\"</p>
            locale: <p>A string containing the geographical region or location of the user.</p>
            timezone: <p>A string containing the time zone of the user.</p>
            photos: <p>A list of photos associated with the user. You can add up to 3 photos per user. Each photo can include a value, type, display name, and primary designation.</p>
            website: <p>The user's personal website or blog URL. This field allows users to provide a link to their personal or professional website.</p>
            birthdate: <p>The user's birthdate in YYYY-MM-DD format. This field supports standard date format for storing personal information.</p>
            roles: <p>A list of <code>Role</code> objects containing roles associated with the user.</p>
            extensions: <p>A map with additional attribute extensions for the user. Each map key corresponds to an extension name, while map values represent extension data in <code>Document</code> type (not supported by Java V1, Go V1 and older versions of the CLI). <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.create_user_request.CreateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.create_user

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if user_name is not None:
            input_["user_name"] = user_name
        if name is not None:
            input_["name"] = name
        if display_name is not None:
            input_["display_name"] = display_name
        if nick_name is not None:
            input_["nick_name"] = nick_name
        if profile_url is not None:
            input_["profile_url"] = profile_url
        if emails is not None:
            input_["emails"] = emails
        if addresses is not None:
            input_["addresses"] = addresses
        if phone_numbers is not None:
            input_["phone_numbers"] = phone_numbers
        if user_type is not None:
            input_["user_type"] = user_type
        if title is not None:
            input_["title"] = title
        if preferred_language is not None:
            input_["preferred_language"] = preferred_language
        if locale is not None:
            input_["locale"] = locale
        if timezone is not None:
            input_["timezone"] = timezone
        if photos is not None:
            input_["photos"] = photos
        if website is not None:
            input_["website"] = website
        if birthdate is not None:
            input_["birthdate"] = birthdate
        if roles is not None:
            input_["roles"] = roles
        if extensions is not None:
            input_["extensions"] = extensions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        extensions: Optional[
            "aws_sdk_identitystore.types.extension_names.ExtensionNames"
        ] = None,
    ) -> "aws_sdk_identitystore.types.describe_user_response.DescribeUserResponse":
        r"""<p>Retrieves the user metadata and attributes from the <code>UserId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            user_id: <p>The identifier for a user in the identity store.</p>
            extensions: <p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.describe_user_request.DescribeUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.describe_user_response.DescribeUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.describe_user

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.describe_user.async_describe_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.describe_user_request.DescribeUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["user_id"] = user_id
        if extensions is not None:
            input_["extensions"] = extensions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        operations: "aws_sdk_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.update_user_response.UpdateUserResponse":
        r"""<p>Updates the specified user metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_id: <p>The identifier for a user in the identity store.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested user. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html\">User</a>.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.update_user_request.UpdateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.update_user

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.update_user.async_update_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["user_id"] = user_id
        input_["operations"] = operations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        user_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user within an identity store given <code>UserId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            user_id: <p>The identifier for a user in the identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.delete_user_request.DeleteUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.delete_user_response.DeleteUserResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.delete_user

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.delete_user.async_delete_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        extensions: Optional[
            "aws_sdk_identitystore.types.extension_names.ExtensionNames"
        ] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_identitystore.types.filters.Filters"] = None,
    ) -> "aws_sdk_identitystore.types.list_users_response.ListUsersResponse":
        r"""<p>Lists all users in the identity store. Returns a paginated list of complete <code>User</code> objects. Filtering for a <code>User</code> by the <code>UserName</code> attribute is deprecated. Instead, use the <code>GetUserId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            extensions: <p>A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests. </p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.list_users_request.ListUsersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.list_users_response.ListUsersResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_users

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.list_users.async_list_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_users_request.ListUsersRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if extensions is not None:
            input_["extensions"] = extensions
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
