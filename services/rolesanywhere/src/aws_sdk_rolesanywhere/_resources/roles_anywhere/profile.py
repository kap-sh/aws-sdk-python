from typing import TYPE_CHECKING, Optional

import aws_sdk_rolesanywhere._auth._signers
import aws_sdk_rolesanywhere._auth._sigv4
from aws_sdk_rolesanywhere._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.certificate_field
    import aws_sdk_rolesanywhere.types.create_profile_request
    import aws_sdk_rolesanywhere.types.delete_attribute_mapping_request
    import aws_sdk_rolesanywhere.types.delete_attribute_mapping_response
    import aws_sdk_rolesanywhere.types.list_profiles_response
    import aws_sdk_rolesanywhere.types.list_request
    import aws_sdk_rolesanywhere.types.managed_policy_list
    import aws_sdk_rolesanywhere.types.mapping_rules
    import aws_sdk_rolesanywhere.types.profile_detail
    import aws_sdk_rolesanywhere.types.profile_detail_response
    import aws_sdk_rolesanywhere.types.put_attribute_mapping_request
    import aws_sdk_rolesanywhere.types.put_attribute_mapping_response
    import aws_sdk_rolesanywhere.types.resource_name
    import aws_sdk_rolesanywhere.types.role_arn_list
    import aws_sdk_rolesanywhere.types.scalar_profile_request
    import aws_sdk_rolesanywhere.types.specifier_list
    import aws_sdk_rolesanywhere.types.tag_list
    import aws_sdk_rolesanywhere.types.update_profile_request
    import aws_sdk_rolesanywhere.types.uuid
    from aws_sdk_rolesanywhere._services.async_roles_anywhere import (
        AsyncRolesAnywhereClient,
        AsyncRolesAnywhereClientConfig,
    )
    from aws_sdk_rolesanywhere._services.roles_anywhere import (
        RolesAnywhereClient,
        RolesAnywhereClientConfig,
    )


class Profile:
    def __init__(self, service: RolesAnywhereClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_rolesanywhere.types.resource_name.ResourceName",
        role_arns: "aws_sdk_rolesanywhere.types.role_arn_list.RoleArnList",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        require_instance_properties: Optional[bool] = None,
        session_policy: Optional[str] = None,
        managed_policy_arns: Optional[
            "aws_sdk_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
        ] = None,
        duration_seconds: Optional[int] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_rolesanywhere.types.tag_list.TagList"] = None,
        accept_role_session_name: Optional[bool] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Creates a <i>profile</i>, a list of the roles that Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:CreateProfile</code>. </p>

        Args:
            name: <p>The name of the profile.</p>
            require_instance_properties: <p>Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile. </p>
            session_policy: <p>A session policy that applies to the trust boundary of the vended session credentials. </p>
            role_arns: <p>A list of IAM roles that this profile can assume in a temporary credential request.</p>
            managed_policy_arns: <p>A list of managed policy ARNs that apply to the vended session credentials. </p>
            duration_seconds: <p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href=\"https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object\">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>
            enabled: <p>Specifies whether the profile is enabled.</p>
            tags: <p>The tags to attach to the profile.</p>
            accept_role_session_name: <p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.create_profile_request.CreateProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.create_profile

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.create_profile.create_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.create_profile_request.CreateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if require_instance_properties is not None:
            input_["require_instance_properties"] = require_instance_properties
        if session_policy is not None:
            input_["session_policy"] = session_policy
        input_["role_arns"] = role_arns
        if managed_policy_arns is not None:
            input_["managed_policy_arns"] = managed_policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if accept_role_session_name is not None:
            input_["accept_role_session_name"] = accept_role_session_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Gets a profile.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_profile

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.get_profile.get_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        name: Optional["aws_sdk_rolesanywhere.types.resource_name.ResourceName"] = None,
        session_policy: Optional[str] = None,
        role_arns: Optional[
            "aws_sdk_rolesanywhere.types.role_arn_list.RoleArnList"
        ] = None,
        managed_policy_arns: Optional[
            "aws_sdk_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
        ] = None,
        duration_seconds: Optional[int] = None,
        accept_role_session_name: Optional[bool] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Updates a <i>profile</i>, a list of the roles that IAM Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            name: <p>The name of the profile.</p>
            session_policy: <p>A session policy that applies to the trust boundary of the vended session credentials. </p>
            role_arns: <p>A list of IAM roles that this profile can assume in a temporary credential request.</p>
            managed_policy_arns: <p>A list of managed policy ARNs that apply to the vended session credentials. </p>
            duration_seconds: <p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href=\"https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object\">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>
            accept_role_session_name: <p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.update_profile_request.UpdateProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.update_profile

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.update_profile.update_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.update_profile_request.UpdateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        if name is not None:
            input_["name"] = name
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if role_arns is not None:
            input_["role_arns"] = role_arns
        if managed_policy_arns is not None:
            input_["managed_policy_arns"] = managed_policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if accept_role_session_name is not None:
            input_["accept_role_session_name"] = accept_role_session_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Deletes a profile.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_profile

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.delete_profile.delete_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_profiles_response.ListProfilesResponse":
        """<p>Lists all profiles in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListProfiles</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.list_profiles_response.ListProfilesResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_profiles

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.list_profiles.list_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.list_request.ListRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_attribute_mapping(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        certificate_field: "aws_sdk_rolesanywhere.types.certificate_field.CertificateField",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        specifiers: Optional[
            "aws_sdk_rolesanywhere.types.specifier_list.SpecifierList"
        ] = None,
    ) -> "aws_sdk_rolesanywhere.types.delete_attribute_mapping_response.DeleteAttributeMappingResponse":
        """<p>Delete an entry from the attribute mapping rules enforced by a given profile.</p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            certificate_field: <p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>
            specifiers: <p>A list of specifiers of a certificate field; for example, CN, OU, UID from a Subject.</p>

        Examples:
            DeleteAttributeMapping - Deletes a custom attribute mapping rule

            >>> client.delete_attribute_mapping(profile_id='00000000-0000-0000-0000-000000000000', specifiers=['OU'], certificate_field='x509Subject')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.delete_attribute_mapping_request.DeleteAttributeMappingRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.delete_attribute_mapping_response.DeleteAttributeMappingResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_attribute_mapping

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.delete_attribute_mapping.delete_attribute_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.delete_attribute_mapping_request.DeleteAttributeMappingRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["certificate_field"] = certificate_field
        if specifiers is not None:
            input_["specifiers"] = specifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_profile(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Disables a profile. When disabled, temporary credential requests with this profile fail.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.disable_profile

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.disable_profile.disable_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_profile(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Enables temporary credential requests for a profile. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.enable_profile

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.enable_profile.enable_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_attribute_mapping(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        certificate_field: "aws_sdk_rolesanywhere.types.certificate_field.CertificateField",
        mapping_rules: "aws_sdk_rolesanywhere.types.mapping_rules.MappingRules",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.put_attribute_mapping_response.PutAttributeMappingResponse":
        """<p>Put an entry in the attribute mapping rules that will be enforced by a given profile. A mapping specifies a certificate field and one or more specifiers that have contextual meanings.</p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            certificate_field: <p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>
            mapping_rules: <p>A list of mapping entries for every supported specifier or sub-field.</p>

        Examples:
            PutAttributeMapping - Adds a custom attribute mapping rule

            >>> client.put_attribute_mapping(profile_id='00000000-0000-0000-0000-000000000000', mapping_rules=[{'specifier': 'CN'}], certificate_field='x509Subject')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.put_attribute_mapping_request.PutAttributeMappingRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.put_attribute_mapping_response.PutAttributeMappingResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.put_attribute_mapping

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.put_attribute_mapping.put_attribute_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.put_attribute_mapping_request.PutAttributeMappingRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["certificate_field"] = certificate_field
        input_["mapping_rules"] = mapping_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncProfile:
    def __init__(self, service: AsyncRolesAnywhereClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_rolesanywhere.types.resource_name.ResourceName",
        role_arns: "aws_sdk_rolesanywhere.types.role_arn_list.RoleArnList",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        require_instance_properties: Optional[bool] = None,
        session_policy: Optional[str] = None,
        managed_policy_arns: Optional[
            "aws_sdk_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
        ] = None,
        duration_seconds: Optional[int] = None,
        enabled: Optional[bool] = None,
        tags: Optional["aws_sdk_rolesanywhere.types.tag_list.TagList"] = None,
        accept_role_session_name: Optional[bool] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Creates a <i>profile</i>, a list of the roles that Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:CreateProfile</code>. </p>

        Args:
            name: <p>The name of the profile.</p>
            require_instance_properties: <p>Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile. </p>
            session_policy: <p>A session policy that applies to the trust boundary of the vended session credentials. </p>
            role_arns: <p>A list of IAM roles that this profile can assume in a temporary credential request.</p>
            managed_policy_arns: <p>A list of managed policy ARNs that apply to the vended session credentials. </p>
            duration_seconds: <p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href=\"https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object\">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>
            enabled: <p>Specifies whether the profile is enabled.</p>
            tags: <p>The tags to attach to the profile.</p>
            accept_role_session_name: <p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.create_profile_request.CreateProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.create_profile

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.create_profile_request.CreateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if require_instance_properties is not None:
            input_["require_instance_properties"] = require_instance_properties
        if session_policy is not None:
            input_["session_policy"] = session_policy
        input_["role_arns"] = role_arns
        if managed_policy_arns is not None:
            input_["managed_policy_arns"] = managed_policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags
        if accept_role_session_name is not None:
            input_["accept_role_session_name"] = accept_role_session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Gets a profile.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_profile

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["aws_sdk_rolesanywhere.types.resource_name.ResourceName"] = None,
        session_policy: Optional[str] = None,
        role_arns: Optional[
            "aws_sdk_rolesanywhere.types.role_arn_list.RoleArnList"
        ] = None,
        managed_policy_arns: Optional[
            "aws_sdk_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
        ] = None,
        duration_seconds: Optional[int] = None,
        accept_role_session_name: Optional[bool] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Updates a <i>profile</i>, a list of the roles that IAM Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            name: <p>The name of the profile.</p>
            session_policy: <p>A session policy that applies to the trust boundary of the vended session credentials. </p>
            role_arns: <p>A list of IAM roles that this profile can assume in a temporary credential request.</p>
            managed_policy_arns: <p>A list of managed policy ARNs that apply to the vended session credentials. </p>
            duration_seconds: <p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href=\"https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object\">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>
            accept_role_session_name: <p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.update_profile_request.UpdateProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.update_profile

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.update_profile_request.UpdateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        if name is not None:
            input_["name"] = name
        if session_policy is not None:
            input_["session_policy"] = session_policy
        if role_arns is not None:
            input_["role_arns"] = role_arns
        if managed_policy_arns is not None:
            input_["managed_policy_arns"] = managed_policy_arns
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if accept_role_session_name is not None:
            input_["accept_role_session_name"] = accept_role_session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Deletes a profile.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_profile

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_profiles_response.ListProfilesResponse":
        """<p>Lists all profiles in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListProfiles</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.list_profiles_response.ListProfilesResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.list_request.ListRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_attribute_mapping(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        certificate_field: "aws_sdk_rolesanywhere.types.certificate_field.CertificateField",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        specifiers: Optional[
            "aws_sdk_rolesanywhere.types.specifier_list.SpecifierList"
        ] = None,
    ) -> "aws_sdk_rolesanywhere.types.delete_attribute_mapping_response.DeleteAttributeMappingResponse":
        """<p>Delete an entry from the attribute mapping rules enforced by a given profile.</p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            certificate_field: <p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>
            specifiers: <p>A list of specifiers of a certificate field; for example, CN, OU, UID from a Subject.</p>

        Examples:
            DeleteAttributeMapping - Deletes a custom attribute mapping rule

            >>> await client.delete_attribute_mapping(profile_id='00000000-0000-0000-0000-000000000000', specifiers=['OU'], certificate_field='x509Subject')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.delete_attribute_mapping_request.DeleteAttributeMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.delete_attribute_mapping_response.DeleteAttributeMappingResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.delete_attribute_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.delete_attribute_mapping.async_delete_attribute_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.delete_attribute_mapping_request.DeleteAttributeMappingRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["certificate_field"] = certificate_field
        if specifiers is not None:
            input_["specifiers"] = specifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_profile(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Disables a profile. When disabled, temporary credential requests with this profile fail.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.disable_profile

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.disable_profile.async_disable_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_profile(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse":
        """<p>Enables temporary credential requests for a profile. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableProfile</code>. </p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.profile_detail_response.ProfileDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.enable_profile

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.enable_profile.async_enable_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_profile_request.ScalarProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_attribute_mapping(
        self,
        profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        certificate_field: "aws_sdk_rolesanywhere.types.certificate_field.CertificateField",
        mapping_rules: "aws_sdk_rolesanywhere.types.mapping_rules.MappingRules",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.put_attribute_mapping_response.PutAttributeMappingResponse":
        """<p>Put an entry in the attribute mapping rules that will be enforced by a given profile. A mapping specifies a certificate field and one or more specifiers that have contextual meanings.</p>

        Args:
            profile_id: <p>The unique identifier of the profile.</p>
            certificate_field: <p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>
            mapping_rules: <p>A list of mapping entries for every supported specifier or sub-field.</p>

        Examples:
            PutAttributeMapping - Adds a custom attribute mapping rule

            >>> await client.put_attribute_mapping(profile_id='00000000-0000-0000-0000-000000000000', mapping_rules=[{'specifier': 'CN'}], certificate_field='x509Subject')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.put_attribute_mapping_request.PutAttributeMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.put_attribute_mapping_response.PutAttributeMappingResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.put_attribute_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.put_attribute_mapping.async_put_attribute_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.put_attribute_mapping_request.PutAttributeMappingRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["certificate_field"] = certificate_field
        input_["mapping_rules"] = mapping_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
