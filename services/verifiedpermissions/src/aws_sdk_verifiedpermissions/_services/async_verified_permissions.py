"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#VerifiedPermissions``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_verifiedpermissions._auth._signers
import aws_sdk_verifiedpermissions._auth._sigv4
from aws_sdk_verifiedpermissions._auth._identity import Credentials
from aws_sdk_verifiedpermissions._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_verifiedpermissions._auth._zapros_handler import AuthMiddleware
from aws_sdk_verifiedpermissions._resources.verified_permissions.policy_store import (
    AsyncPolicyStore,
)
from aws_sdk_verifiedpermissions._resources.verified_permissions.policy_store_alias import (
    AsyncPolicyStoreAlias,
)
from aws_sdk_verifiedpermissions._services._aws_config import aaws_config
from aws_sdk_verifiedpermissions._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.amazon_resource_name
    import aws_sdk_verifiedpermissions.types.list_tags_for_resource_input
    import aws_sdk_verifiedpermissions.types.list_tags_for_resource_output
    import aws_sdk_verifiedpermissions.types.tag_key_list
    import aws_sdk_verifiedpermissions.types.tag_map
    import aws_sdk_verifiedpermissions.types.tag_resource_input
    import aws_sdk_verifiedpermissions.types.tag_resource_output
    import aws_sdk_verifiedpermissions.types.untag_resource_input
    import aws_sdk_verifiedpermissions.types.untag_resource_output


class AsyncVerifiedPermissionsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncVerifiedPermissionsClient:
    """A client for the ``VerifiedPermissions`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncVerifiedPermissionsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.policy_store = AsyncPolicyStore(self)
        self.policy_store_alias = AsyncPolicyStoreAlias(self)

    def operation_options(
        self, config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncVerifiedPermissionsClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_verifiedpermissions.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns the tags associated with the specified Amazon Verified Permissions resource. In Verified Permissions, policy stores can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to view tags.</p>

        Raises:
            aws_sdk_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            aws_sdk_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            aws_sdk_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            aws_sdk_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href=\"https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test\">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href=\"https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test\">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            aws_sdk_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            aws_sdk_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListTagsForResource
            The following example lists all the tags for the resource named in the API call.

            >>> await client.list_tags_for_resource(resource_arn='C7v5xMplfFH3i3e4Jrzb1a')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_verifiedpermissions.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_verifiedpermissions.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified Amazon Verified Permissions resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Verified Permissions, policy stores can be tagged.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the TagResource action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you're adding tags to.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

        Raises:
            aws_sdk_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            aws_sdk_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            aws_sdk_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            aws_sdk_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href=\"https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test\">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href=\"https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test\">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            aws_sdk_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            aws_sdk_verifiedpermissions.errors.too_many_tags_exception.TooManyTagsException: <p>No more tags be added because the limit (50) has been reached. To add new tags, use <code>UntagResource</code> to remove existing tags.</p>
            aws_sdk_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            TagResource
            The following example tags the resource.

            >>> await client.tag_resource(resource_arn='C7v5xMplfFH3i3e4Jrzb1a', tags={'key1': 'value1', 'key2': 'value2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_verifiedpermissions.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_verifiedpermissions.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncVerifiedPermissionsClientConfig] = None,
    ) -> "aws_sdk_verifiedpermissions.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified Amazon Verified Permissions resource. In Verified Permissions, policy stores can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource from which you are removing tags.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            aws_sdk_verifiedpermissions.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            aws_sdk_verifiedpermissions.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error. Try your request again later</p>
            aws_sdk_verifiedpermissions.errors.throttling_exception.ThrottlingException: <p>The request failed because it exceeded a throttling quota.</p>
            aws_sdk_verifiedpermissions.errors.validation_exception.ValidationException: <p>The request failed because one or more input parameters don't satisfy their constraint requirements. The output is provided as a list of fields and a reason for each field that isn't valid.</p> <p>The possible reasons include the following:</p> <ul> <li> <p> <b>UnrecognizedEntityType</b> </p> <p>The policy includes an entity type that isn't found in the schema.</p> </li> <li> <p> <b>UnrecognizedActionId</b> </p> <p>The policy includes an action id that isn't found in the schema.</p> </li> <li> <p> <b>InvalidActionApplication</b> </p> <p>The policy includes an action that, according to the schema, doesn't support the specified principal and resource.</p> </li> <li> <p> <b>UnexpectedType</b> </p> <p>The policy included an operand that isn't a valid type for the specified operation.</p> </li> <li> <p> <b>IncompatibleTypes</b> </p> <p>The types of elements included in a <code>set</code>, or the types of expressions used in an <code>if...then...else</code> clause aren't compatible in this context.</p> </li> <li> <p> <b>MissingAttribute</b> </p> <p>The policy attempts to access a record or entity attribute that isn't specified in the schema. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href=\"https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test\">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>UnsafeOptionalAttributeAccess</b> </p> <p>The policy attempts to access a record or entity attribute that is optional and isn't guaranteed to be present. Test for the existence of the attribute first before attempting to access its value. For more information, see the <a href=\"https://docs.cedarpolicy.com/policies/syntax-operators.html#has-presence-of-attribute-test\">has (presence of attribute test) operator</a> in the <i>Cedar Policy Language Guide</i>.</p> </li> <li> <p> <b>ImpossiblePolicy</b> </p> <p>Cedar has determined that a policy condition always evaluates to false. If the policy is always false, it can never apply to any query, and so it can never affect an authorization decision.</p> </li> <li> <p> <b>WrongNumberArguments</b> </p> <p>The policy references an extension type with the wrong number of arguments.</p> </li> <li> <p> <b>FunctionArgumentValidationError</b> </p> <p>Cedar couldn't parse the argument passed to an extension type. For example, a string that is to be parsed as an IPv4 address can contain only digits and the period character.</p> </li> </ul>
            aws_sdk_verifiedpermissions.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request failed because it references a resource that doesn't exist.</p>
            aws_sdk_verifiedpermissions.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UntagResource
            The following example removes the listed tags from the resource.

            >>> await client.untag_resource(resource_arn='C7v5xMplfFH3i3e4Jrzb1a', tag_keys=['key1', 'key2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_verifiedpermissions.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_verifiedpermissions.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_verifiedpermissions._operations.verified_permissions.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_verifiedpermissions._operations.verified_permissions.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_verifiedpermissions.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
