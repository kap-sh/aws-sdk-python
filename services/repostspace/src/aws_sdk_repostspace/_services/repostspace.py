"""Generated from Smithy shape ``com.amazonaws.repostspace#RepostSpace``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_repostspace._auth._signers
import aws_sdk_repostspace._auth._sigv4
from aws_sdk_repostspace._auth._identity import Credentials
from aws_sdk_repostspace._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_repostspace._auth._zapros_handler import AuthMiddleware
from aws_sdk_repostspace._pagination import resolve_path as _resolve_path
from aws_sdk_repostspace._services._aws_config import aws_config
from aws_sdk_repostspace._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.admin_id
    import aws_sdk_repostspace.types.arn
    import aws_sdk_repostspace.types.batch_add_channel_role_to_accessors_input
    import aws_sdk_repostspace.types.batch_add_channel_role_to_accessors_output
    import aws_sdk_repostspace.types.batch_add_role_input
    import aws_sdk_repostspace.types.batch_add_role_output
    import aws_sdk_repostspace.types.batch_remove_channel_role_from_accessors_input
    import aws_sdk_repostspace.types.batch_remove_channel_role_from_accessors_output
    import aws_sdk_repostspace.types.batch_remove_role_input
    import aws_sdk_repostspace.types.batch_remove_role_output
    import aws_sdk_repostspace.types.channel_data
    import aws_sdk_repostspace.types.channel_description
    import aws_sdk_repostspace.types.channel_id
    import aws_sdk_repostspace.types.channel_name
    import aws_sdk_repostspace.types.channel_role
    import aws_sdk_repostspace.types.create_channel_input
    import aws_sdk_repostspace.types.create_channel_output
    import aws_sdk_repostspace.types.create_space_input
    import aws_sdk_repostspace.types.create_space_output
    import aws_sdk_repostspace.types.delete_space_input
    import aws_sdk_repostspace.types.deregister_admin_input
    import aws_sdk_repostspace.types.get_channel_input
    import aws_sdk_repostspace.types.get_channel_output
    import aws_sdk_repostspace.types.get_space_input
    import aws_sdk_repostspace.types.get_space_output
    import aws_sdk_repostspace.types.invite_body
    import aws_sdk_repostspace.types.invite_title
    import aws_sdk_repostspace.types.kms_key
    import aws_sdk_repostspace.types.list_channels_input
    import aws_sdk_repostspace.types.list_channels_limit
    import aws_sdk_repostspace.types.list_channels_output
    import aws_sdk_repostspace.types.list_spaces_input
    import aws_sdk_repostspace.types.list_spaces_limit
    import aws_sdk_repostspace.types.list_spaces_output
    import aws_sdk_repostspace.types.list_tags_for_resource_request
    import aws_sdk_repostspace.types.list_tags_for_resource_response
    import aws_sdk_repostspace.types.register_admin_input
    import aws_sdk_repostspace.types.role
    import aws_sdk_repostspace.types.send_invites_input
    import aws_sdk_repostspace.types.space_data
    import aws_sdk_repostspace.types.space_description
    import aws_sdk_repostspace.types.space_id
    import aws_sdk_repostspace.types.space_name
    import aws_sdk_repostspace.types.space_subdomain
    import aws_sdk_repostspace.types.supported_email_domains_parameters
    import aws_sdk_repostspace.types.tag_key_list
    import aws_sdk_repostspace.types.tag_resource_request
    import aws_sdk_repostspace.types.tag_resource_response
    import aws_sdk_repostspace.types.tags
    import aws_sdk_repostspace.types.tier_level
    import aws_sdk_repostspace.types.untag_resource_request
    import aws_sdk_repostspace.types.untag_resource_response
    import aws_sdk_repostspace.types.update_channel_input
    import aws_sdk_repostspace.types.update_channel_output
    import aws_sdk_repostspace.types.update_space_input


class repostspaceClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class repostspaceClient:
    """A client for the ``repostspace`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = repostspaceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[repostspaceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: repostspaceClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_add_channel_role_to_accessors(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId",
        accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList",
        channel_role: "aws_sdk_repostspace.types.channel_role.ChannelRole",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.batch_add_channel_role_to_accessors_output.BatchAddChannelRoleToAccessorsOutput":
        """<p>Add role to multiple users or groups in a private re:Post channel.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            channel_id: <p>The unique ID of the private re:Post channel.</p>
            accessor_ids: <p>The user or group identifiers to add the role to.</p>
            channel_role: <p>The channel role to add to the users or groups.</p>

        Examples:
            BatchAddChannelRoleToAccessors

            >>> client.batch_add_channel_role_to_accessors(space_id='SP1234567890abcdefghijkl', channel_id='WS1234567890abcdefghijkl', accessor_ids=['12345678-1234-1234-1234-1234567890ab'], channel_role='MODERATOR')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.batch_add_channel_role_to_accessors_input.BatchAddChannelRoleToAccessorsInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.batch_add_channel_role_to_accessors_output.BatchAddChannelRoleToAccessorsOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.batch_add_channel_role_to_accessors

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.batch_add_channel_role_to_accessors.batch_add_channel_role_to_accessors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.batch_add_channel_role_to_accessors_input.BatchAddChannelRoleToAccessorsInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["channel_id"] = channel_id
        input_["accessor_ids"] = accessor_ids
        input_["channel_role"] = channel_role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_add_role(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList",
        role: "aws_sdk_repostspace.types.role.Role",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.batch_add_role_output.BatchAddRoleOutput":
        """<p>Add a role to multiple users or groups in a private re:Post.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            accessor_ids: <p>The user or group accessor identifiers to add the role to.</p>
            role: <p>The role to add to the users or groups.</p>

        Examples:
            BatchAddRole

            >>> client.batch_add_role(space_id='SP1234567890abcdefghijkl', accessor_ids=['12345678-1234-1234-1234-1234567890ab'], role='EXPERT')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.batch_add_role_input.BatchAddRoleInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.batch_add_role_output.BatchAddRoleOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.batch_add_role

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.batch_add_role.batch_add_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.batch_add_role_input.BatchAddRoleInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["accessor_ids"] = accessor_ids
        input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_remove_channel_role_from_accessors(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId",
        accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList",
        channel_role: "aws_sdk_repostspace.types.channel_role.ChannelRole",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.batch_remove_channel_role_from_accessors_output.BatchRemoveChannelRoleFromAccessorsOutput":
        """<p>Remove a role from multiple users or groups in a private re:Post channel.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            channel_id: <p>The unique ID of the private re:Post channel.</p>
            accessor_ids: <p>The users or groups identifiers to remove the role from.</p>
            channel_role: <p>The channel role to remove from the users or groups.</p>

        Examples:
            BatchRemoveChannelRoleFromAccessors

            >>> client.batch_remove_channel_role_from_accessors(space_id='SP1234567890abcdefghijkl', channel_id='WS1234567890abcdefghijkl', accessor_ids=['12345678-1234-1234-1234-1234567890ab'], channel_role='MODERATOR')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.batch_remove_channel_role_from_accessors_input.BatchRemoveChannelRoleFromAccessorsInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.batch_remove_channel_role_from_accessors_output.BatchRemoveChannelRoleFromAccessorsOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.batch_remove_channel_role_from_accessors

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.batch_remove_channel_role_from_accessors.batch_remove_channel_role_from_accessors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.batch_remove_channel_role_from_accessors_input.BatchRemoveChannelRoleFromAccessorsInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["channel_id"] = channel_id
        input_["accessor_ids"] = accessor_ids
        input_["channel_role"] = channel_role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_remove_role(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList",
        role: "aws_sdk_repostspace.types.role.Role",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.batch_remove_role_output.BatchRemoveRoleOutput":
        """<p>Remove a role from multiple users or groups in a private re:Post.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            accessor_ids: <p>The user or group accessor identifiers to remove the role from.</p>
            role: <p>The role to remove from the users or groups.</p>

        Examples:
            BatchRemoveRole

            >>> client.batch_remove_role(space_id='SP1234567890abcdefghijkl', accessor_ids=['12345678-1234-1234-1234-1234567890ab'], role='EXPERT')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.batch_remove_role_input.BatchRemoveRoleInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.batch_remove_role_output.BatchRemoveRoleOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.batch_remove_role

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.batch_remove_role.batch_remove_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.batch_remove_role_input.BatchRemoveRoleInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["accessor_ids"] = accessor_ids
        input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        channel_name: "aws_sdk_repostspace.types.channel_name.ChannelName",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        channel_description: Optional[
            "aws_sdk_repostspace.types.channel_description.ChannelDescription"
        ] = None,
    ) -> "aws_sdk_repostspace.types.create_channel_output.CreateChannelOutput":
        """<p>Creates a channel in an AWS re:Post Private private re:Post.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            channel_name: <p>The name for the channel. This must be unique per private re:Post.</p>
            channel_description: <p>A description for the channel. This is used only to help you identify this channel.</p>

        Examples:
            CreateChannel

            >>> client.create_channel(space_id='SP1234567890abcdefghijkl', channel_name='My First Channel', channel_description='Useful channel description')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.create_channel_input.CreateChannelInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.create_channel_output.CreateChannelOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.create_channel

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.create_channel_input.CreateChannelInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["channel_name"] = channel_name
        if channel_description is not None:
            input_["channel_description"] = channel_description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_space(
        self,
        name: "aws_sdk_repostspace.types.space_name.SpaceName",
        subdomain: "aws_sdk_repostspace.types.space_subdomain.SpaceSubdomain",
        tier: "aws_sdk_repostspace.types.tier_level.TierLevel",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        description: Optional[
            "aws_sdk_repostspace.types.space_description.SpaceDescription"
        ] = None,
        user_kms_key: Optional["aws_sdk_repostspace.types.kms_key.KMSKey"] = None,
        tags: Optional["aws_sdk_repostspace.types.tags.Tags"] = None,
        role_arn: Optional["aws_sdk_repostspace.types.arn.Arn"] = None,
        supported_email_domains: Optional[
            "aws_sdk_repostspace.types.supported_email_domains_parameters.SupportedEmailDomainsParameters"
        ] = None,
    ) -> "aws_sdk_repostspace.types.create_space_output.CreateSpaceOutput":
        """<p>Creates an AWS re:Post Private private re:Post.</p>

        Args:
            name: <p>The name for the private re:Post. This must be unique in your account.</p>
            subdomain: <p>The subdomain that you use to access your AWS re:Post Private private re:Post. All custom subdomains must be approved by AWS before use. In addition to your custom subdomain, all private re:Posts are issued an AWS generated subdomain for immediate use.</p>
            tier: <p>The pricing tier for the private re:Post.</p>
            description: <p>A description for the private re:Post. This is used only to help you identify this private re:Post.</p>
            user_kms_key: <p>The AWS KMS key ARN that’s used for the AWS KMS encryption. If you don't provide a key, your data is encrypted by default with a key that AWS owns and manages for you.</p>
            tags: <p>The list of tags associated with the private re:Post.</p>
            role_arn: <p>The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.</p>
            supported_email_domains: <p/>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.create_space_input.CreateSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.create_space_output.CreateSpaceOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.create_space

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.create_space.create_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.create_space_input.CreateSpaceInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["subdomain"] = subdomain
        input_["tier"] = tier
        if description is not None:
            input_["description"] = description
        if user_kms_key is not None:
            input_["user_kms_key"] = user_kms_key
        if tags is not None:
            input_["tags"] = tags
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if supported_email_domains is not None:
            input_["supported_email_domains"] = supported_email_domains

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_space(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> None:
        """<p>Deletes an AWS re:Post Private private re:Post.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.delete_space_input.DeleteSpaceInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_repostspace._operations.repost_space.delete_space

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.delete_space.delete_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.delete_space_input.DeleteSpaceInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_admin(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        admin_id: "aws_sdk_repostspace.types.admin_id.AdminId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> None:
        """<p>Removes the user or group from the list of administrators of the private re:Post.</p>

        Args:
            space_id: <p>The ID of the private re:Post to remove the admin from.</p>
            admin_id: <p>The ID of the admin to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.deregister_admin_input.DeregisterAdminInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_repostspace._operations.repost_space.deregister_admin

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.deregister_admin.deregister_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.deregister_admin_input.DeregisterAdminInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["admin_id"] = admin_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_channel(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.get_channel_output.GetChannelOutput":
        """<p>Displays information about a channel in a private re:Post.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            channel_id: <p>The unique ID of the private re:Post channel.</p>

        Examples:
            GetChannel

            >>> client.get_channel(space_id='SP1234567890abcdefghijkl', channel_id='WS1234567890abcdefghijkl')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.get_channel_input.GetChannelInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.get_channel_output.GetChannelOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.get_channel

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.get_channel.get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.get_channel_input.GetChannelInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["channel_id"] = channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_space(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.get_space_output.GetSpaceOutput":
        """<p>Displays information about the AWS re:Post Private private re:Post.</p>

        Args:
            space_id: <p>The ID of the private re:Post.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.get_space_input.GetSpaceInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.get_space_output.GetSpaceOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.get_space

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.get_space.get_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.get_space_input.GetSpaceInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channels(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_repostspace.types.list_channels_limit.ListChannelsLimit"
        ] = None,
    ) -> "aws_sdk_repostspace.types.list_channels_output.ListChannelsOutput":
        """<p>Returns the list of channel within a private re:Post with some information about each channel.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            next_token: <p>The token for the next set of channel to return. You receive this token from a previous ListChannels operation.</p>
            max_results: <p>The maximum number of channels to include in the results.</p>

        Examples:
            ListChannels

            >>> client.list_channels(space_id='SP1234567890abcdefghijkl')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.list_channels_input.ListChannelsInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.list_channels_output.ListChannelsOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.list_channels

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.list_channels_input.ListChannelsInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_channels(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_repostspace.types.list_channels_limit.ListChannelsLimit"
        ] = None,
    ) -> "Iterator[aws_sdk_repostspace.types.channel_data.ChannelData]":
        _token = next_token
        while True:
            _response = self.list_channels(
                space_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_spaces(
        self,
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_repostspace.types.list_spaces_limit.ListSpacesLimit"
        ] = None,
    ) -> "aws_sdk_repostspace.types.list_spaces_output.ListSpacesOutput":
        """<p>Returns a list of AWS re:Post Private private re:Posts in the account with some information about each private re:Post.</p>

        Args:
            next_token: <p>The token for the next set of private re:Posts to return. You receive this token from a previous ListSpaces operation.</p>
            max_results: <p>The maximum number of private re:Posts to include in the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.list_spaces_input.ListSpacesInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.list_spaces_output.ListSpacesOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.list_spaces

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.list_spaces.list_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.list_spaces_input.ListSpacesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_spaces(
        self,
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_repostspace.types.list_spaces_limit.ListSpacesLimit"
        ] = None,
    ) -> "Iterator[aws_sdk_repostspace.types.space_data.SpaceData]":
        _token = next_token
        while True:
            _response = self.list_spaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("spaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_repostspace.types.arn.Arn",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the tags that are associated with the AWS re:Post Private resource specified by the resourceArn. The only resource that can be tagged is a private re:Post.</p>

        Args:
            resource_arn: <p>The ARN of the resource that the tags are associated with.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_repostspace._operations.repost_space.list_tags_for_resource

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_admin(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        admin_id: "aws_sdk_repostspace.types.admin_id.AdminId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> None:
        """<p>Adds a user or group to the list of administrators of the private re:Post.</p>

        Args:
            space_id: <p>The ID of the private re:Post.</p>
            admin_id: <p>The ID of the administrator.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.register_admin_input.RegisterAdminInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_repostspace._operations.repost_space.register_admin

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.register_admin.register_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.register_admin_input.RegisterAdminInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["admin_id"] = admin_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_invites(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList",
        title: "aws_sdk_repostspace.types.invite_title.InviteTitle",
        body: "aws_sdk_repostspace.types.invite_body.InviteBody",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> None:
        """<p>Sends an invitation email to selected users and groups.</p>

        Args:
            space_id: <p>The ID of the private re:Post.</p>
            accessor_ids: <p>The array of identifiers for the users and groups.</p>
            title: <p>The title of the invite.</p>
            body: <p>The body of the invite.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.send_invites_input.SendInvitesInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_repostspace._operations.repost_space.send_invites

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.send_invites.send_invites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.send_invites_input.SendInvitesInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["accessor_ids"] = accessor_ids
        input_["title"] = title
        input_["body"] = body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_repostspace.types.arn.Arn",
        tags: "aws_sdk_repostspace.types.tags.Tags",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.tag_resource_response.TagResourceResponse":
        """<p>Associates tags with an AWS re:Post Private resource. Currently, the only resource that can be tagged is the private re:Post. If you specify a new tag key for the resource, the tag is appended to the list of tags that are associated with the resource. If you specify a tag key that’s already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource that the tag is associated with.</p>
            tags: <p>The list of tag keys and values that must be associated with the resource. You can associate tag keys only, tags (key and values) only, or a combination of tag keys and tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_repostspace._operations.repost_space.tag_resource

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_repostspace.types.arn.Arn",
        tag_keys: "aws_sdk_repostspace.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
    ) -> "aws_sdk_repostspace.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the association of the tag with the AWS re:Post Private resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>The key values of the tag.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_repostspace._operations.repost_space.untag_resource

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId",
        channel_name: "aws_sdk_repostspace.types.channel_name.ChannelName",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        channel_description: Optional[
            "aws_sdk_repostspace.types.channel_description.ChannelDescription"
        ] = None,
    ) -> "aws_sdk_repostspace.types.update_channel_output.UpdateChannelOutput":
        """<p>Modifies an existing channel.</p>

        Args:
            space_id: <p>The unique ID of the private re:Post.</p>
            channel_id: <p>The unique ID of the private re:Post channel.</p>
            channel_name: <p>The name for the channel. This must be unique per private re:Post.</p>
            channel_description: <p>A description for the channel. This is used only to help you identify this channel.</p>

        Examples:
            UpdateChannel

            >>> client.update_channel(space_id='SP1234567890abcdefghijkl', channel_id='WS1234567890abcdefghijkl', channel_name='Better Channel', channel_description='Better channel description')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.update_channel_input.UpdateChannelInput]",
        ) -> OperationResponse[
            "aws_sdk_repostspace.types.update_channel_output.UpdateChannelOutput"
        ]:
            import aws_sdk_repostspace._operations.repost_space.update_channel

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.update_channel_input.UpdateChannelInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        input_["channel_id"] = channel_id
        input_["channel_name"] = channel_name
        if channel_description is not None:
            input_["channel_description"] = channel_description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_space(
        self,
        space_id: "aws_sdk_repostspace.types.space_id.SpaceId",
        *,
        config_overrides: Optional[repostspaceClientConfig] = None,
        description: Optional[
            "aws_sdk_repostspace.types.space_description.SpaceDescription"
        ] = None,
        tier: Optional["aws_sdk_repostspace.types.tier_level.TierLevel"] = None,
        role_arn: Optional["aws_sdk_repostspace.types.arn.Arn"] = None,
        supported_email_domains: Optional[
            "aws_sdk_repostspace.types.supported_email_domains_parameters.SupportedEmailDomainsParameters"
        ] = None,
    ) -> None:
        """<p>Modifies an existing AWS re:Post Private private re:Post.</p>

        Args:
            space_id: <p>The unique ID of this private re:Post.</p>
            description: <p>A description for the private re:Post. This is used only to help you identify this private re:Post.</p>
            tier: <p>The pricing tier of this private re:Post.</p>
            role_arn: <p>The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.</p>
            supported_email_domains: <p/>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_repostspace.types.update_space_input.UpdateSpaceInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_repostspace._operations.repost_space.update_space

            output, http_response = (
                aws_sdk_repostspace._operations.repost_space.update_space.update_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_repostspace.types.update_space_input.UpdateSpaceInput = {}  # type: ignore[typeddict-item]
        input_["space_id"] = space_id
        if description is not None:
            input_["description"] = description
        if tier is not None:
            input_["tier"] = tier
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if supported_email_domains is not None:
            input_["supported_email_domains"] = supported_email_domains

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
