"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AmazonCloudDirectory_20170111``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_clouddirectory._auth._signers
import aws_sdk_clouddirectory._auth._sigv4
from aws_sdk_clouddirectory._auth._identity import Credentials
from aws_sdk_clouddirectory._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_clouddirectory._auth._zapros_handler import AuthMiddleware
from aws_sdk_clouddirectory._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.add_facet_to_object_request
    import aws_sdk_clouddirectory.types.add_facet_to_object_response
    import aws_sdk_clouddirectory.types.apply_schema_request
    import aws_sdk_clouddirectory.types.apply_schema_response
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.attach_object_request
    import aws_sdk_clouddirectory.types.attach_object_response
    import aws_sdk_clouddirectory.types.attach_policy_request
    import aws_sdk_clouddirectory.types.attach_policy_response
    import aws_sdk_clouddirectory.types.attach_to_index_request
    import aws_sdk_clouddirectory.types.attach_to_index_response
    import aws_sdk_clouddirectory.types.attach_typed_link_request
    import aws_sdk_clouddirectory.types.attach_typed_link_response
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list
    import aws_sdk_clouddirectory.types.attribute_key_list
    import aws_sdk_clouddirectory.types.attribute_name_and_value_list
    import aws_sdk_clouddirectory.types.attribute_name_list
    import aws_sdk_clouddirectory.types.batch_read_operation_list
    import aws_sdk_clouddirectory.types.batch_read_request
    import aws_sdk_clouddirectory.types.batch_read_response
    import aws_sdk_clouddirectory.types.batch_write_operation_list
    import aws_sdk_clouddirectory.types.batch_write_request
    import aws_sdk_clouddirectory.types.batch_write_response
    import aws_sdk_clouddirectory.types.bool
    import aws_sdk_clouddirectory.types.consistency_level
    import aws_sdk_clouddirectory.types.create_directory_request
    import aws_sdk_clouddirectory.types.create_directory_response
    import aws_sdk_clouddirectory.types.create_facet_request
    import aws_sdk_clouddirectory.types.create_facet_response
    import aws_sdk_clouddirectory.types.create_index_request
    import aws_sdk_clouddirectory.types.create_index_response
    import aws_sdk_clouddirectory.types.create_object_request
    import aws_sdk_clouddirectory.types.create_object_response
    import aws_sdk_clouddirectory.types.create_schema_request
    import aws_sdk_clouddirectory.types.create_schema_response
    import aws_sdk_clouddirectory.types.create_typed_link_facet_request
    import aws_sdk_clouddirectory.types.create_typed_link_facet_response
    import aws_sdk_clouddirectory.types.delete_directory_request
    import aws_sdk_clouddirectory.types.delete_directory_response
    import aws_sdk_clouddirectory.types.delete_facet_request
    import aws_sdk_clouddirectory.types.delete_facet_response
    import aws_sdk_clouddirectory.types.delete_object_request
    import aws_sdk_clouddirectory.types.delete_object_response
    import aws_sdk_clouddirectory.types.delete_schema_request
    import aws_sdk_clouddirectory.types.delete_schema_response
    import aws_sdk_clouddirectory.types.delete_typed_link_facet_request
    import aws_sdk_clouddirectory.types.delete_typed_link_facet_response
    import aws_sdk_clouddirectory.types.detach_from_index_request
    import aws_sdk_clouddirectory.types.detach_from_index_response
    import aws_sdk_clouddirectory.types.detach_object_request
    import aws_sdk_clouddirectory.types.detach_object_response
    import aws_sdk_clouddirectory.types.detach_policy_request
    import aws_sdk_clouddirectory.types.detach_policy_response
    import aws_sdk_clouddirectory.types.detach_typed_link_request
    import aws_sdk_clouddirectory.types.directory_arn
    import aws_sdk_clouddirectory.types.directory_name
    import aws_sdk_clouddirectory.types.directory_state
    import aws_sdk_clouddirectory.types.disable_directory_request
    import aws_sdk_clouddirectory.types.disable_directory_response
    import aws_sdk_clouddirectory.types.enable_directory_request
    import aws_sdk_clouddirectory.types.enable_directory_response
    import aws_sdk_clouddirectory.types.facet_attribute_list
    import aws_sdk_clouddirectory.types.facet_attribute_update_list
    import aws_sdk_clouddirectory.types.facet_name
    import aws_sdk_clouddirectory.types.facet_style
    import aws_sdk_clouddirectory.types.get_applied_schema_version_request
    import aws_sdk_clouddirectory.types.get_applied_schema_version_response
    import aws_sdk_clouddirectory.types.get_directory_request
    import aws_sdk_clouddirectory.types.get_directory_response
    import aws_sdk_clouddirectory.types.get_facet_request
    import aws_sdk_clouddirectory.types.get_facet_response
    import aws_sdk_clouddirectory.types.get_link_attributes_request
    import aws_sdk_clouddirectory.types.get_link_attributes_response
    import aws_sdk_clouddirectory.types.get_object_attributes_request
    import aws_sdk_clouddirectory.types.get_object_attributes_response
    import aws_sdk_clouddirectory.types.get_object_information_request
    import aws_sdk_clouddirectory.types.get_object_information_response
    import aws_sdk_clouddirectory.types.get_schema_as_json_request
    import aws_sdk_clouddirectory.types.get_schema_as_json_response
    import aws_sdk_clouddirectory.types.get_typed_link_facet_information_request
    import aws_sdk_clouddirectory.types.get_typed_link_facet_information_response
    import aws_sdk_clouddirectory.types.link_attribute_update_list
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.list_applied_schema_arns_request
    import aws_sdk_clouddirectory.types.list_applied_schema_arns_response
    import aws_sdk_clouddirectory.types.list_attached_indices_request
    import aws_sdk_clouddirectory.types.list_attached_indices_response
    import aws_sdk_clouddirectory.types.list_development_schema_arns_request
    import aws_sdk_clouddirectory.types.list_development_schema_arns_response
    import aws_sdk_clouddirectory.types.list_directories_request
    import aws_sdk_clouddirectory.types.list_directories_response
    import aws_sdk_clouddirectory.types.list_facet_attributes_request
    import aws_sdk_clouddirectory.types.list_facet_attributes_response
    import aws_sdk_clouddirectory.types.list_facet_names_request
    import aws_sdk_clouddirectory.types.list_facet_names_response
    import aws_sdk_clouddirectory.types.list_incoming_typed_links_request
    import aws_sdk_clouddirectory.types.list_incoming_typed_links_response
    import aws_sdk_clouddirectory.types.list_index_request
    import aws_sdk_clouddirectory.types.list_index_response
    import aws_sdk_clouddirectory.types.list_managed_schema_arns_request
    import aws_sdk_clouddirectory.types.list_managed_schema_arns_response
    import aws_sdk_clouddirectory.types.list_object_attributes_request
    import aws_sdk_clouddirectory.types.list_object_attributes_response
    import aws_sdk_clouddirectory.types.list_object_children_request
    import aws_sdk_clouddirectory.types.list_object_children_response
    import aws_sdk_clouddirectory.types.list_object_parent_paths_request
    import aws_sdk_clouddirectory.types.list_object_parent_paths_response
    import aws_sdk_clouddirectory.types.list_object_parents_request
    import aws_sdk_clouddirectory.types.list_object_parents_response
    import aws_sdk_clouddirectory.types.list_object_policies_request
    import aws_sdk_clouddirectory.types.list_object_policies_response
    import aws_sdk_clouddirectory.types.list_outgoing_typed_links_request
    import aws_sdk_clouddirectory.types.list_outgoing_typed_links_response
    import aws_sdk_clouddirectory.types.list_policy_attachments_request
    import aws_sdk_clouddirectory.types.list_policy_attachments_response
    import aws_sdk_clouddirectory.types.list_published_schema_arns_request
    import aws_sdk_clouddirectory.types.list_published_schema_arns_response
    import aws_sdk_clouddirectory.types.list_tags_for_resource_request
    import aws_sdk_clouddirectory.types.list_tags_for_resource_response
    import aws_sdk_clouddirectory.types.list_typed_link_facet_attributes_request
    import aws_sdk_clouddirectory.types.list_typed_link_facet_attributes_response
    import aws_sdk_clouddirectory.types.list_typed_link_facet_names_request
    import aws_sdk_clouddirectory.types.list_typed_link_facet_names_response
    import aws_sdk_clouddirectory.types.lookup_policy_request
    import aws_sdk_clouddirectory.types.lookup_policy_response
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.number_results
    import aws_sdk_clouddirectory.types.object_attribute_range_list
    import aws_sdk_clouddirectory.types.object_attribute_update_list
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.object_type
    import aws_sdk_clouddirectory.types.publish_schema_request
    import aws_sdk_clouddirectory.types.publish_schema_response
    import aws_sdk_clouddirectory.types.put_schema_from_json_request
    import aws_sdk_clouddirectory.types.put_schema_from_json_response
    import aws_sdk_clouddirectory.types.remove_facet_from_object_request
    import aws_sdk_clouddirectory.types.remove_facet_from_object_response
    import aws_sdk_clouddirectory.types.schema_facet
    import aws_sdk_clouddirectory.types.schema_facet_list
    import aws_sdk_clouddirectory.types.schema_json_document
    import aws_sdk_clouddirectory.types.schema_name
    import aws_sdk_clouddirectory.types.tag_key_list
    import aws_sdk_clouddirectory.types.tag_list
    import aws_sdk_clouddirectory.types.tag_resource_request
    import aws_sdk_clouddirectory.types.tag_resource_response
    import aws_sdk_clouddirectory.types.tags_number_results
    import aws_sdk_clouddirectory.types.typed_link_attribute_range_list
    import aws_sdk_clouddirectory.types.typed_link_facet
    import aws_sdk_clouddirectory.types.typed_link_facet_attribute_update_list
    import aws_sdk_clouddirectory.types.typed_link_name
    import aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name
    import aws_sdk_clouddirectory.types.typed_link_specifier
    import aws_sdk_clouddirectory.types.untag_resource_request
    import aws_sdk_clouddirectory.types.untag_resource_response
    import aws_sdk_clouddirectory.types.update_facet_request
    import aws_sdk_clouddirectory.types.update_facet_response
    import aws_sdk_clouddirectory.types.update_link_attributes_request
    import aws_sdk_clouddirectory.types.update_link_attributes_response
    import aws_sdk_clouddirectory.types.update_object_attributes_request
    import aws_sdk_clouddirectory.types.update_object_attributes_response
    import aws_sdk_clouddirectory.types.update_schema_request
    import aws_sdk_clouddirectory.types.update_schema_response
    import aws_sdk_clouddirectory.types.update_typed_link_facet_request
    import aws_sdk_clouddirectory.types.update_typed_link_facet_response
    import aws_sdk_clouddirectory.types.upgrade_applied_schema_request
    import aws_sdk_clouddirectory.types.upgrade_applied_schema_response
    import aws_sdk_clouddirectory.types.upgrade_published_schema_request
    import aws_sdk_clouddirectory.types.upgrade_published_schema_response
    import aws_sdk_clouddirectory.types.version


class AsyncCloudDirectoryClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncCloudDirectoryClient:
    """A client for the ``CloudDirectory`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncCloudDirectoryClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudDirectoryClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def add_facet_to_object(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        schema_facet: "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        object_attribute_list: Optional[
            "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.add_facet_to_object_response.AddFacetToObjectResponse":
        """<p>Adds a new <a>Facet</a> to an object. An object can have more than one facet applied on it.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>
            schema_facet: <p>Identifiers for the facet that you are adding to the object. See <a>SchemaFacet</a> for details.</p>
            object_attribute_list: <p>Attributes on the facet that you are adding to the object.</p>
            object_reference: <p>A reference to the object you are adding the specified facet to.</p>

        Examples:
            To add a facet to an object

            >>> await client.add_facet_to_object(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', schema_facet={'SchemaArn': 'arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1', 'FacetName': 'node1'}, object_attribute_list=[], object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWmspn1fxfQmSQaaVKSbvEiQ'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.add_facet_to_object_request.AddFacetToObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.add_facet_to_object_response.AddFacetToObjectResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.add_facet_to_object

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.add_facet_to_object.async_add_facet_to_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.add_facet_to_object_request.AddFacetToObjectRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["schema_facet"] = schema_facet
        if object_attribute_list is not None:
            input_["object_attribute_list"] = object_attribute_list
        input_["object_reference"] = object_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def apply_schema(
        self,
        published_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.apply_schema_response.ApplySchemaResponse":
        """<p>Copies the input published schema, at the specified version, into the <a>Directory</a> with the same name and version as that of the published schema.</p>

        Args:
            published_schema_arn: <p>Published schema Amazon Resource Name (ARN) that needs to be copied. For more information, see <a>arns</a>.</p>
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> into which the schema is copied. For more information, see <a>arns</a>.</p>

        Examples:
            To apply a schema

            >>> await client.apply_schema(published_schema_arn='arn:aws:clouddirectory:us-west-2:45132example:schema/published/org/1', directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.apply_schema_request.ApplySchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.apply_schema_response.ApplySchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.apply_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.apply_schema.async_apply_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.apply_schema_request.ApplySchemaRequest = {}  # type: ignore[typeddict-item]
        input_["published_schema_arn"] = published_schema_arn
        input_["directory_arn"] = directory_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_object(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        parent_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        child_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        link_name: "aws_sdk_clouddirectory.types.link_name.LinkName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.attach_object_response.AttachObjectResponse":
        """<p>Attaches an existing object to another object. An object can be accessed in two ways:</p> <ol> <li> <p>Using the path</p> </li> <li> <p>Using <code>ObjectIdentifier</code> </p> </li> </ol>

        Args:
            directory_arn: <p>Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.</p>
            parent_reference: <p>The parent object reference.</p>
            child_reference: <p>The child object reference to be attached to the object.</p>
            link_name: <p>The link name with which the child object is attached to the parent.</p>

        Examples:
            To attach an object

            >>> await client.attach_object(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', parent_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'}, child_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA'}, link_name='link2')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.attach_object_request.AttachObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.attach_object_response.AttachObjectResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_object

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_object.async_attach_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.attach_object_request.AttachObjectRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["parent_reference"] = parent_reference
        input_["child_reference"] = child_reference
        input_["link_name"] = link_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_policy(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        policy_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.attach_policy_response.AttachPolicyResponse":
        """<p>Attaches a policy object to a regular object. An object can have a limited number of attached policies.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.</p>
            policy_reference: <p>The reference that is associated with the policy object.</p>
            object_reference: <p>The reference that identifies the object to which the policy will be attached.</p>

        Examples:
            To attach a policy to an object

            >>> await client.attach_policy(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', policy_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWgcBsTVmcQEWs6jlygfhuew'}, object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWQoovm1s3Ts2v0NKrzdVnPw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.attach_policy_request.AttachPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.attach_policy_response.AttachPolicyResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_policy

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_policy.async_attach_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.attach_policy_request.AttachPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["policy_reference"] = policy_reference
        input_["object_reference"] = object_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_to_index(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.attach_to_index_response.AttachToIndexResponse":
        """<p>Attaches the specified object to the specified index.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) of the directory where the object and index exist.</p>
            index_reference: <p>A reference to the index that you are attaching the object to.</p>
            target_reference: <p>A reference to the object that you are attaching to the index.</p>

        Examples:
            To attach a index to an object

            >>> await client.attach_to_index(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', index_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TW45F26R1HTY2z-stwKBte_Q'}, target_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.attach_to_index_request.AttachToIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.attach_to_index_response.AttachToIndexResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_to_index

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_to_index.async_attach_to_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.attach_to_index_request.AttachToIndexRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["index_reference"] = index_reference
        input_["target_reference"] = target_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def attach_typed_link(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        source_object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        target_object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        typed_link_facet: "aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.TypedLinkSchemaAndFacetName",
        attributes: "aws_sdk_clouddirectory.types.attribute_name_and_value_list.AttributeNameAndValueList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse":
        """<p>Attaches a typed link to a specified source and target object. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) of the directory where you want to attach the typed link.</p>
            source_object_reference: <p>Identifies the source object that the typed link will attach to.</p>
            target_object_reference: <p>Identifies the target object that the typed link will attach to.</p>
            typed_link_facet: <p>Identifies the typed link facet that is associated with the typed link.</p>
            attributes: <p>A set of attributes that are associated with the typed link.</p>

        Examples:
            To attach a typed link to an object

            >>> await client.attach_typed_link(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', source_object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA'}, target_object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'}, typed_link_facet={'TypedLinkName': 'exampletypedlink8', 'SchemaArn': 'arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1'}, attributes=[{'AttributeName': '22', 'Value': {'BinaryValue': 'c3Ry'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.attach_typed_link_request.AttachTypedLinkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_typed_link

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.attach_typed_link.async_attach_typed_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.attach_typed_link_request.AttachTypedLinkRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["source_object_reference"] = source_object_reference
        input_["target_object_reference"] = target_object_reference
        input_["typed_link_facet"] = typed_link_facet
        input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_read(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        operations: "aws_sdk_clouddirectory.types.batch_read_operation_list.BatchReadOperationList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.batch_read_response.BatchReadResponse":
        """<p>Performs all the read operations in a batch. </p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>
            operations: <p>A list of operations that are part of the batch.</p>
            consistency_level: <p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>

        Examples:
            To run a batch read command

            >>> await client.batch_read(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', operations=[], consistency_level='EVENTUAL')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.batch_read_request.BatchReadRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.batch_read_response.BatchReadResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.batch_read

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.batch_read.async_batch_read(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.batch_read_request.BatchReadRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["operations"] = operations
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_write(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        operations: "aws_sdk_clouddirectory.types.batch_write_operation_list.BatchWriteOperationList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.batch_write_response.BatchWriteResponse":
        """<p>Performs all the write operations in a batch. Either all the operations succeed or none.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>
            operations: <p>A list of operations that are part of the batch.</p>

        Examples:
            To run a batch write command

            >>> await client.batch_write(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', operations=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.batch_write_request.BatchWriteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.batch_write_response.BatchWriteResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.batch_write

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.batch_write.async_batch_write(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.batch_write_request.BatchWriteRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["operations"] = operations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_directory(
        self,
        name: "aws_sdk_clouddirectory.types.directory_name.DirectoryName",
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> (
        "aws_sdk_clouddirectory.types.create_directory_response.CreateDirectoryResponse"
    ):
        """<p>Creates a <a>Directory</a> by copying the published schema into the directory. A directory cannot be created without a schema.</p> <p>You can also quickly create a directory using a managed schema, called the <code>QuickStartSchema</code>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_managed.html\">Managed Schema</a> in the <i>Amazon Cloud Directory Developer Guide</i>.</p>

        Args:
            name: <p>The name of the <a>Directory</a>. Should be unique per account, per region.</p>
            schema_arn: <p>The Amazon Resource Name (ARN) of the published schema that will be copied into the data <a>Directory</a>. For more information, see <a>arns</a>.</p>

        Examples:
            To create a new Cloud Directory

            >>> await client.create_directory(name='ExampleCD', schema_arn='arn:aws:clouddirectory:us-west-2:45132example:schema/published/person/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.create_directory_request.CreateDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.create_directory_response.CreateDirectoryResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_directory

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_directory.async_create_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.create_directory_request.CreateDirectoryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["schema_arn"] = schema_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.facet_name.FacetName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        attributes: Optional[
            "aws_sdk_clouddirectory.types.facet_attribute_list.FacetAttributeList"
        ] = None,
        object_type: Optional[
            "aws_sdk_clouddirectory.types.object_type.ObjectType"
        ] = None,
        facet_style: Optional[
            "aws_sdk_clouddirectory.types.facet_style.FacetStyle"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.create_facet_response.CreateFacetResponse":
        """<p>Creates a new <a>Facet</a> in a schema. Facet creation is allowed only in development or applied schemas.</p>

        Args:
            schema_arn: <p>The schema ARN in which the new <a>Facet</a> will be created. For more information, see <a>arns</a>.</p>
            name: <p>The name of the <a>Facet</a>, which is unique for a given schema.</p>
            attributes: <p>The attributes that are associated with the <a>Facet</a>.</p>
            object_type: <p>Specifies whether a given object created from this facet is of type node, leaf node, policy or index.</p> <ul> <li> <p>Node: Can have multiple children but one parent.</p> </li> </ul> <ul> <li> <p>Leaf node: Cannot have children but can have multiple parents.</p> </li> </ul> <ul> <li> <p>Policy: Allows you to store a policy document and policy type. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies\">Policies</a>.</p> </li> </ul> <ul> <li> <p>Index: Can be created with the Index API.</p> </li> </ul>
            facet_style: <p>There are two different styles that you can define on any given facet, <code>Static</code> and <code>Dynamic</code>. For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.</p>

        Examples:
            To create a facet

            >>> await client.create_facet(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1', name='node1', object_type='NODE')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.create_facet_request.CreateFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.create_facet_response.CreateFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_facet.async_create_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.create_facet_request.CreateFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name
        if attributes is not None:
            input_["attributes"] = attributes
        if object_type is not None:
            input_["object_type"] = object_type
        if facet_style is not None:
            input_["facet_style"] = facet_style

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_index(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        ordered_indexed_attribute_list: "aws_sdk_clouddirectory.types.attribute_key_list.AttributeKeyList",
        is_unique: "aws_sdk_clouddirectory.types.bool.Bool",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        parent_reference: Optional[
            "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
        ] = None,
        link_name: Optional["aws_sdk_clouddirectory.types.link_name.LinkName"] = None,
    ) -> "aws_sdk_clouddirectory.types.create_index_response.CreateIndexResponse":
        """<p>Creates an index object. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.html\">Indexing and search</a> for more information.</p>

        Args:
            directory_arn: <p>The ARN of the directory where the index should be created.</p>
            ordered_indexed_attribute_list: <p>Specifies the attributes that should be indexed on. Currently only a single attribute is supported.</p>
            is_unique: <p>Indicates whether the attribute that is being indexed has unique values or not.</p>
            parent_reference: <p>A reference to the parent object that contains the index object.</p>
            link_name: <p>The name of the link between the parent object and the index object.</p>

        Examples:
            To create an index

            >>> await client.create_index(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8', ordered_indexed_attribute_list=[], is_unique=True, parent_reference={}, link_name='Examplelink')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.create_index_request.CreateIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.create_index_response.CreateIndexResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_index

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_index.async_create_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.create_index_request.CreateIndexRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["ordered_indexed_attribute_list"] = ordered_indexed_attribute_list
        input_["is_unique"] = is_unique
        if parent_reference is not None:
            input_["parent_reference"] = parent_reference
        if link_name is not None:
            input_["link_name"] = link_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_object(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        schema_facets: "aws_sdk_clouddirectory.types.schema_facet_list.SchemaFacetList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        object_attribute_list: Optional[
            "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
        ] = None,
        parent_reference: Optional[
            "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
        ] = None,
        link_name: Optional["aws_sdk_clouddirectory.types.link_name.LinkName"] = None,
    ) -> "aws_sdk_clouddirectory.types.create_object_response.CreateObjectResponse":
        """<p>Creates an object in a <a>Directory</a>. Additionally attaches the object to a parent, if a parent reference and <code>LinkName</code> is specified. An object is simply a collection of <a>Facet</a> attributes. You can also use this API call to create a policy object, if the facet from which you create the object is a policy facet. </p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> in which the object will be created. For more information, see <a>arns</a>.</p>
            schema_facets: <p>A list of schema facets to be associated with the object. Do not provide minor version components. See <a>SchemaFacet</a> for details.</p>
            object_attribute_list: <p>The attribute map whose attribute ARN contains the key and attribute value as the map value.</p>
            parent_reference: <p>If specified, the parent reference to which this object will be attached.</p>
            link_name: <p>The name of link that is used to attach this object to a parent.</p>

        Examples:
            To create an object

            >>> await client.create_object(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8', schema_facets=[{'SchemaArn': 'arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8/schema/ExampleOrgPersonSchema/1', 'FacetName': 'Organization_Person'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.create_object_request.CreateObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.create_object_response.CreateObjectResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_object

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_object.async_create_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.create_object_request.CreateObjectRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["schema_facets"] = schema_facets
        if object_attribute_list is not None:
            input_["object_attribute_list"] = object_attribute_list
        if parent_reference is not None:
            input_["parent_reference"] = parent_reference
        if link_name is not None:
            input_["link_name"] = link_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_schema(
        self,
        name: "aws_sdk_clouddirectory.types.schema_name.SchemaName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.create_schema_response.CreateSchemaResponse":
        """<p>Creates a new schema in a development state. A schema can exist in three phases:</p> <ul> <li> <p> <i>Development:</i> This is a mutable phase of the schema. All new schemas are in the development phase. Once the schema is finalized, it can be published.</p> </li> <li> <p> <i>Published:</i> Published schemas are immutable and have a version associated with them.</p> </li> <li> <p> <i>Applied:</i> Applied schemas are mutable in a way that allows you to add new schema facets. You can also add new, nonrequired attributes to existing schema facets. You can apply only published schemas to directories. </p> </li> </ul>

        Args:
            name: <p>The name that is associated with the schema. This is unique to each account and in each region.</p>

        Examples:
            To create a schema

            >>> await client.create_schema(name='Customers')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.create_schema_request.CreateSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.create_schema_response.CreateSchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_schema.async_create_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.create_schema_request.CreateSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_typed_link_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        facet: "aws_sdk_clouddirectory.types.typed_link_facet.TypedLinkFacet",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.create_typed_link_facet_response.CreateTypedLinkFacetResponse":
        """<p>Creates a <a>TypedLinkFacet</a>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>
            facet: <p> <a>Facet</a> structure that is associated with the typed link facet.</p>

        Examples:
            To create a typed link facet

            >>> await client.create_typed_link_facet(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:schema/development/typedlinkschema', facet={'Name': 'FacetExample', 'Attributes': [{'Name': '1', 'Type': 'BINARY', 'RequiredBehavior': 'REQUIRED_ALWAYS'}], 'IdentityAttributeOrder': ['1']})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.create_typed_link_facet_request.CreateTypedLinkFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.create_typed_link_facet_response.CreateTypedLinkFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_typed_link_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.create_typed_link_facet.async_create_typed_link_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.create_typed_link_facet_request.CreateTypedLinkFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["facet"] = facet

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_directory(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> (
        "aws_sdk_clouddirectory.types.delete_directory_response.DeleteDirectoryResponse"
    ):
        """<p>Deletes a directory. Only disabled directories can be deleted. A deleted directory cannot be undone. Exercise extreme caution when deleting directories.</p>

        Args:
            directory_arn: <p>The ARN of the directory to delete.</p>

        Examples:
            To delete a directory

            >>> await client.delete_directory(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.delete_directory_request.DeleteDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.delete_directory_response.DeleteDirectoryResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_directory

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_directory.async_delete_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.delete_directory_request.DeleteDirectoryRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.facet_name.FacetName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.delete_facet_response.DeleteFacetResponse":
        """<p>Deletes a given <a>Facet</a>. All attributes and <a>Rule</a>s that are associated with the facet will be deleted. Only development schema facets are allowed deletion.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>
            name: <p>The name of the facet to delete.</p>

        Examples:
            To delete a facet

            >>> await client.delete_facet(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:schema/development/exampleorgtest', name='Organization')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.delete_facet_request.DeleteFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.delete_facet_response.DeleteFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_facet.async_delete_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.delete_facet_request.DeleteFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_object(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.delete_object_response.DeleteObjectResponse":
        """<p>Deletes an object and its associated attributes. Only objects with no children and no parents can be deleted. The maximum number of attributes that can be deleted during an object deletion is 30. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html\">Amazon Cloud Directory Limits</a>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>
            object_reference: <p>A reference that identifies the object.</p>

        Examples:
            To delete an object

            >>> await client.delete_object(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI', object_reference={'Selector': '$AQHzK-KsptZGU78KjmnwGH6i8H-voMZDSNCqfx-fRUcBFg'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.delete_object_request.DeleteObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.delete_object_response.DeleteObjectResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_object

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_object.async_delete_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.delete_object_request.DeleteObjectRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_schema(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.delete_schema_response.DeleteSchemaResponse":
        """<p>Deletes a given schema. Schemas in a development and published state can only be deleted. </p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.</p>

        Examples:
            To delete a schema

            >>> await client.delete_schema(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:schema/development/exampleorgtest')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.delete_schema_request.DeleteSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.delete_schema_response.DeleteSchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_schema.async_delete_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.delete_schema_request.DeleteSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_typed_link_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.delete_typed_link_facet_response.DeleteTypedLinkFacetResponse":
        """<p>Deletes a <a>TypedLinkFacet</a>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>
            name: <p>The unique name of the typed link facet.</p>

        Examples:
            To delete a typed link facet

            >>> await client.delete_typed_link_facet(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:schema/development/typedlinkschematest', name='ExampleFacet')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.delete_typed_link_facet_request.DeleteTypedLinkFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.delete_typed_link_facet_response.DeleteTypedLinkFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_typed_link_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.delete_typed_link_facet.async_delete_typed_link_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.delete_typed_link_facet_request.DeleteTypedLinkFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def detach_from_index(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.detach_from_index_response.DetachFromIndexResponse":
        """<p>Detaches the specified object from the specified index.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) of the directory the index and object exist in.</p>
            index_reference: <p>A reference to the index object.</p>
            target_reference: <p>A reference to the object being detached from the index.</p>

        Examples:
            To detach an object from an index

            >>> await client.detach_from_index(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', index_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TW45F26R1HTY2z-stwKBte_Q'}, target_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.detach_from_index_request.DetachFromIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.detach_from_index_response.DetachFromIndexResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_from_index

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_from_index.async_detach_from_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.detach_from_index_request.DetachFromIndexRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["index_reference"] = index_reference
        input_["target_reference"] = target_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def detach_object(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        parent_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        link_name: "aws_sdk_clouddirectory.types.link_name.LinkName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.detach_object_response.DetachObjectResponse":
        """<p>Detaches a given object from the parent object. The object that is to be detached from the parent is specified by the link name.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.</p>
            parent_reference: <p>The parent reference from which the object with the specified link name is detached.</p>
            link_name: <p>The link name associated with the object that needs to be detached.</p>

        Examples:
            To detach an object from its parent object

            >>> await client.detach_object(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', parent_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'}, link_name='link2')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.detach_object_request.DetachObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.detach_object_response.DetachObjectResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_object

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_object.async_detach_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.detach_object_request.DetachObjectRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["parent_reference"] = parent_reference
        input_["link_name"] = link_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def detach_policy(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        policy_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.detach_policy_response.DetachPolicyResponse":
        """<p>Detaches a policy from an object.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where both objects reside. For more information, see <a>arns</a>.</p>
            policy_reference: <p>Reference that identifies the policy object.</p>
            object_reference: <p>Reference that identifies the object whose policy object will be detached.</p>

        Examples:
            To detach a policy from an object

            >>> await client.detach_policy(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', policy_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWgcBsTVmcQEWs6jlygfhuew'}, object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWQoovm1s3Ts2v0NKrzdVnPw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.detach_policy_request.DetachPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.detach_policy_response.DetachPolicyResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_policy

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_policy.async_detach_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.detach_policy_request.DetachPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["policy_reference"] = policy_reference
        input_["object_reference"] = object_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def detach_typed_link(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        typed_link_specifier: "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> None:
        """<p>Detaches a typed link from a specified source and target object. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) of the directory where you want to detach the typed link.</p>
            typed_link_specifier: <p>Used to accept a typed link specifier as input.</p>

        Examples:
            To detach a typed link from an object

            >>> await client.detach_typed_link(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', typed_link_specifier={'SourceObjectReference': {'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA'}, 'IdentityAttributeValues': [{'AttributeName': '22', 'Value': {'BinaryValue': 'c3Ry'}}], 'TargetObjectReference': {'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'}, 'TypedLinkFacet': {'TypedLinkName': 'exampletypedlink8', 'SchemaArn': 'arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.detach_typed_link_request.DetachTypedLinkRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_typed_link

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.detach_typed_link.async_detach_typed_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.detach_typed_link_request.DetachTypedLinkRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["typed_link_specifier"] = typed_link_specifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_directory(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.disable_directory_response.DisableDirectoryResponse":
        """<p>Disables the specified directory. Disabled directories cannot be read or written to. Only enabled directories can be disabled. Disabled directories may be reenabled.</p>

        Args:
            directory_arn: <p>The ARN of the directory to disable.</p>

        Examples:
            To disable a directory

            >>> await client.disable_directory(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.disable_directory_request.DisableDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.disable_directory_response.DisableDirectoryResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.disable_directory

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.disable_directory.async_disable_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.disable_directory_request.DisableDirectoryRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_directory(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> (
        "aws_sdk_clouddirectory.types.enable_directory_response.EnableDirectoryResponse"
    ):
        """<p>Enables the specified directory. Only disabled directories can be enabled. Once enabled, the directory can then be read and written to.</p>

        Args:
            directory_arn: <p>The ARN of the directory to enable.</p>

        Examples:
            To enable a disabled directory

            >>> await client.enable_directory(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.enable_directory_request.EnableDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.enable_directory_response.EnableDirectoryResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.enable_directory

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.enable_directory.async_enable_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.enable_directory_request.EnableDirectoryRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_applied_schema_version(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.get_applied_schema_version_response.GetAppliedSchemaVersionResponse":
        """<p>Returns current applied schema version ARN, including the minor version in use.</p>

        Args:
            schema_arn: <p>The ARN of the applied schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_applied_schema_version_request.GetAppliedSchemaVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_applied_schema_version_response.GetAppliedSchemaVersionResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_applied_schema_version

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_applied_schema_version.async_get_applied_schema_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_applied_schema_version_request.GetAppliedSchemaVersionRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_directory(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.directory_arn.DirectoryArn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.get_directory_response.GetDirectoryResponse":
        """<p>Retrieves metadata about a directory.</p>

        Args:
            directory_arn: <p>The ARN of the directory.</p>

        Examples:
            To get information about a directory

            >>> await client.get_directory(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_directory_request.GetDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_directory_response.GetDirectoryResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_directory

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_directory.async_get_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_directory_request.GetDirectoryRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.facet_name.FacetName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.get_facet_response.GetFacetResponse":
        """<p>Gets details of the <a>Facet</a>, such as facet name, attributes, <a>Rule</a>s, or <code>ObjectType</code>. You can call this on all kinds of schema facets -- published, development, or applied.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>
            name: <p>The name of the facet to retrieve.</p>

        Examples:
            To get information about a facet

            >>> await client.get_facet(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1', name='node2')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_facet_request.GetFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_facet_response.GetFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_facet.async_get_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_facet_request.GetFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_link_attributes(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        typed_link_specifier: "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier",
        attribute_names: "aws_sdk_clouddirectory.types.attribute_name_list.AttributeNameList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.get_link_attributes_response.GetLinkAttributesResponse":
        """<p>Retrieves attributes that are associated with a typed link.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the Directory where the typed link resides. For more information, see <a>arns</a> or <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>
            typed_link_specifier: <p>Allows a typed link specifier to be accepted as input.</p>
            attribute_names: <p>A list of attribute names whose values will be retrieved.</p>
            consistency_level: <p>The consistency level at which to retrieve the attributes on a typed link.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_link_attributes_request.GetLinkAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_link_attributes_response.GetLinkAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_link_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_link_attributes.async_get_link_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_link_attributes_request.GetLinkAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["typed_link_specifier"] = typed_link_specifier
        input_["attribute_names"] = attribute_names
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_object_attributes(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        schema_facet: "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet",
        attribute_names: "aws_sdk_clouddirectory.types.attribute_name_list.AttributeNameList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.get_object_attributes_response.GetObjectAttributesResponse":
        """<p>Retrieves attributes within a facet that are associated with an object.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides.</p>
            object_reference: <p>Reference that identifies the object whose attributes will be retrieved.</p>
            consistency_level: <p>The consistency level at which to retrieve the attributes on an object.</p>
            schema_facet: <p>Identifier for the facet whose attributes will be retrieved. See <a>SchemaFacet</a> for details.</p>
            attribute_names: <p>List of attribute names whose values will be retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_object_attributes_request.GetObjectAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_object_attributes_response.GetObjectAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_object_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_object_attributes.async_get_object_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_object_attributes_request.GetObjectAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level
        input_["schema_facet"] = schema_facet
        input_["attribute_names"] = attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_object_information(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.get_object_information_response.GetObjectInformationResponse":
        """<p>Retrieves metadata about an object.</p>

        Args:
            directory_arn: <p>The ARN of the directory being retrieved.</p>
            object_reference: <p>A reference to the object.</p>
            consistency_level: <p>The consistency level at which to retrieve the object information.</p>

        Examples:
            To get information about an object

            >>> await client.get_object_information(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWmspn1fxfQmSQaaVKSbvEiQ'}, consistency_level='SERIALIZABLE')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_object_information_request.GetObjectInformationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_object_information_response.GetObjectInformationResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_object_information

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_object_information.async_get_object_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_object_information_request.GetObjectInformationRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_schema_as_json(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.get_schema_as_json_response.GetSchemaAsJsonResponse":
        """<p>Retrieves a JSON representation of the schema. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_jsonformat.html#schemas_json\">JSON Schema Format</a> for more information.</p>

        Args:
            schema_arn: <p>The ARN of the schema to retrieve.</p>

        Examples:
            To get schema information and display it in JSON format

            >>> await client.get_schema_as_json(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_schema_as_json_request.GetSchemaAsJsonRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_schema_as_json_response.GetSchemaAsJsonResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_schema_as_json

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_schema_as_json.async_get_schema_as_json(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_schema_as_json_request.GetSchemaAsJsonRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_typed_link_facet_information(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.GetTypedLinkFacetInformationResponse":
        """<p>Returns the identity attribute order for a specific <a>TypedLinkFacet</a>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>
            name: <p>The unique name of the typed link facet.</p>

        Examples:
            To get information about a typed link facet

            >>> await client.get_typed_link_facet_information(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1', name='exampletypedlink8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.get_typed_link_facet_information_request.GetTypedLinkFacetInformationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.GetTypedLinkFacetInformationResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_typed_link_facet_information

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.get_typed_link_facet_information.async_get_typed_link_facet_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.get_typed_link_facet_information_request.GetTypedLinkFacetInformationRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_applied_schema_arns(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        schema_arn: Optional["aws_sdk_clouddirectory.types.arn.Arn"] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_applied_schema_arns_response.ListAppliedSchemaArnsResponse":
        """<p>Lists schema major versions applied to a directory. If <code>SchemaArn</code> is provided, lists the minor version.</p>

        Args:
            directory_arn: <p>The ARN of the directory you are listing.</p>
            schema_arn: <p>The response for <code>ListAppliedSchemaArns</code> when this parameter is used will list all minor version ARNs for a major version.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>

        Examples:
            To list applied schema ARNs for a specified directory

            >>> await client.list_applied_schema_arns(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_applied_schema_arns_request.ListAppliedSchemaArnsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_applied_schema_arns_response.ListAppliedSchemaArnsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_applied_schema_arns

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_applied_schema_arns.async_list_applied_schema_arns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_applied_schema_arns_request.ListAppliedSchemaArnsRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        if schema_arn is not None:
            input_["schema_arn"] = schema_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_attached_indices(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        target_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_attached_indices_response.ListAttachedIndicesResponse":
        """<p>Lists indices attached to the specified object.</p>

        Args:
            directory_arn: <p>The ARN of the directory.</p>
            target_reference: <p>A reference to the object that has indices attached.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
            consistency_level: <p>The consistency level to use for this operation.</p>

        Examples:
            To list the indices attached to an object

            >>> await client.list_attached_indices(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', target_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_attached_indices_request.ListAttachedIndicesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_attached_indices_response.ListAttachedIndicesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_attached_indices

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_attached_indices.async_list_attached_indices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_attached_indices_request.ListAttachedIndicesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["target_reference"] = target_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_development_schema_arns(
        self,
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_development_schema_arns_response.ListDevelopmentSchemaArnsResponse":
        """<p>Retrieves each Amazon Resource Name (ARN) of schemas in the development state.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>

        Examples:
            To list all development schema arns in your AWS account

            >>> await client.list_development_schema_arns()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_development_schema_arns_request.ListDevelopmentSchemaArnsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_development_schema_arns_response.ListDevelopmentSchemaArnsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_development_schema_arns

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_development_schema_arns.async_list_development_schema_arns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_development_schema_arns_request.ListDevelopmentSchemaArnsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_directories(
        self,
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        state: Optional[
            "aws_sdk_clouddirectory.types.directory_state.DirectoryState"
        ] = None,
    ) -> (
        "aws_sdk_clouddirectory.types.list_directories_response.ListDirectoriesResponse"
    ):
        """<p>Lists directories created within an account.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
            state: <p>The state of the directories in the list. Can be either Enabled, Disabled, or Deleted.</p>

        Examples:
            To list all directories in your AWS account

            >>> await client.list_directories()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_directories_request.ListDirectoriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_directories_response.ListDirectoriesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_directories

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_directories.async_list_directories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_directories_request.ListDirectoriesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state is not None:
            input_["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_facet_attributes(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.facet_name.FacetName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_facet_attributes_response.ListFacetAttributesResponse":
        """<p>Retrieves attributes attached to the facet.</p>

        Args:
            schema_arn: <p>The ARN of the schema where the facet resides.</p>
            name: <p>The name of the facet whose attributes will be retrieved.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>

        Examples:
            To list facet attributes

            >>> await client.list_facet_attributes(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1', name='Organization')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_facet_attributes_request.ListFacetAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_facet_attributes_response.ListFacetAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_facet_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_facet_attributes.async_list_facet_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_facet_attributes_request.ListFacetAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_facet_names(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> (
        "aws_sdk_clouddirectory.types.list_facet_names_response.ListFacetNamesResponse"
    ):
        """<p>Retrieves the names of facets that exist in a schema.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) to retrieve facet names from.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>

        Examples:
            To list facet names

            >>> await client.list_facet_names(schema_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_facet_names_request.ListFacetNamesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_facet_names_response.ListFacetNamesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_facet_names

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_facet_names.async_list_facet_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_facet_names_request.ListFacetNamesRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_incoming_typed_links(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        filter_attribute_ranges: Optional[
            "aws_sdk_clouddirectory.types.typed_link_attribute_range_list.TypedLinkAttributeRangeList"
        ] = None,
        filter_typed_link: Optional[
            "aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.TypedLinkSchemaAndFacetName"
        ] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_incoming_typed_links_response.ListIncomingTypedLinksResponse":
        """<p>Returns a paginated list of all the incoming <a>TypedLinkSpecifier</a> information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) of the directory where you want to list the typed links.</p>
            object_reference: <p>Reference that identifies the object whose attributes will be listed.</p>
            filter_attribute_ranges: <p>Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.</p>
            filter_typed_link: <p>Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
            consistency_level: <p>The consistency level to execute the request at.</p>

        Examples:
            To list incoming typed links

            >>> await client.list_incoming_typed_links(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_incoming_typed_links_request.ListIncomingTypedLinksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_incoming_typed_links_response.ListIncomingTypedLinksResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_incoming_typed_links

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_incoming_typed_links.async_list_incoming_typed_links(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_incoming_typed_links_request.ListIncomingTypedLinksRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if filter_attribute_ranges is not None:
            input_["filter_attribute_ranges"] = filter_attribute_ranges
        if filter_typed_link is not None:
            input_["filter_typed_link"] = filter_typed_link
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_index(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        index_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        ranges_on_indexed_values: Optional[
            "aws_sdk_clouddirectory.types.object_attribute_range_list.ObjectAttributeRangeList"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_index_response.ListIndexResponse":
        """<p>Lists objects attached to the specified index.</p>

        Args:
            directory_arn: <p>The ARN of the directory that the index exists in.</p>
            ranges_on_indexed_values: <p>Specifies the ranges of indexed values that you want to query.</p>
            index_reference: <p>The reference to the index to list.</p>
            max_results: <p>The maximum number of objects in a single page to retrieve from the index during a request. For more information, see <a href=\"http://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html\">Amazon Cloud Directory Limits</a>.</p>
            next_token: <p>The pagination token.</p>
            consistency_level: <p>The consistency level to execute the request at.</p>

        Examples:
            To list an index

            >>> await client.list_index(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', index_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TW45F26R1HTY2z-stwKBte_Q'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_index_request.ListIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_index_response.ListIndexResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_index

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_index.async_list_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_index_request.ListIndexRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        if ranges_on_indexed_values is not None:
            input_["ranges_on_indexed_values"] = ranges_on_indexed_values
        input_["index_reference"] = index_reference
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_managed_schema_arns(
        self,
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        schema_arn: Optional["aws_sdk_clouddirectory.types.arn.Arn"] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_managed_schema_arns_response.ListManagedSchemaArnsResponse":
        """<p>Lists the major version families of each managed schema. If a major version ARN is provided as SchemaArn, the minor version revisions in that family are listed instead.</p>

        Args:
            schema_arn: <p>The response for ListManagedSchemaArns. When this parameter is used, all minor version ARNs for a major version are listed.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_managed_schema_arns_request.ListManagedSchemaArnsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_managed_schema_arns_response.ListManagedSchemaArnsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_managed_schema_arns

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_managed_schema_arns.async_list_managed_schema_arns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_managed_schema_arns_request.ListManagedSchemaArnsRequest = {}  # type: ignore[typeddict-item]
        if schema_arn is not None:
            input_["schema_arn"] = schema_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_object_attributes(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
        facet_filter: Optional[
            "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_object_attributes_response.ListObjectAttributesResponse":
        """<p>Lists all attributes that are associated with an object. </p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>
            object_reference: <p>The reference that identifies the object whose attributes will be listed.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
            consistency_level: <p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>
            facet_filter: <p>Used to filter the list of object attributes that are associated with a certain facet.</p>

        Examples:
            To list object attributes

            >>> await client.list_object_attributes(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TW45F26R1HTY2z-stwKBte_Q'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_object_attributes_request.ListObjectAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_object_attributes_response.ListObjectAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_attributes.async_list_object_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_object_attributes_request.ListObjectAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level
        if facet_filter is not None:
            input_["facet_filter"] = facet_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_object_children(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_object_children_response.ListObjectChildrenResponse":
        """<p>Returns a paginated list of child objects that are associated with a given object.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>
            object_reference: <p>The reference that identifies the object for which child objects are being listed.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
            consistency_level: <p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>

        Examples:
            To list an objects children

            >>> await client.list_object_children(directory_arn='arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY', object_reference={'Selector': '$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_object_children_request.ListObjectChildrenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_object_children_response.ListObjectChildrenResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_children

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_children.async_list_object_children(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_object_children_request.ListObjectChildrenRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_object_parent_paths(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_object_parent_paths_response.ListObjectParentPathsResponse":
        """<p>Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html\">Directory Structure</a>.</p> <p>Use this API to evaluate all parents for an object. The call returns all objects from the root of the directory up to the requested object. The API returns the number of paths based on user-defined <code>MaxResults</code>, in case there are multiple paths to the parent. The order of the paths and nodes returned is consistent among multiple API calls unless the objects are deleted or moved. Paths not leading to the directory root are ignored from the target object.</p>

        Args:
            directory_arn: <p>The ARN of the directory to which the parent path applies.</p>
            object_reference: <p>The reference that identifies the object whose parent paths are listed.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_object_parent_paths_request.ListObjectParentPathsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_object_parent_paths_response.ListObjectParentPathsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_parent_paths

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_parent_paths.async_list_object_parent_paths(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_object_parent_paths_request.ListObjectParentPathsRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_object_parents(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
        include_all_links_to_each_parent: Optional[
            "aws_sdk_clouddirectory.types.bool.Bool"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_object_parents_response.ListObjectParentsResponse":
        """<p>Lists parent objects that are associated with a given object in pagination fashion.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>
            object_reference: <p>The reference that identifies the object for which parent objects are being listed.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
            consistency_level: <p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>
            include_all_links_to_each_parent: <p>When set to True, returns all <a>ListObjectParentsResponse$ParentLinks</a>. There could be multiple links between a parent-child pair.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_object_parents_request.ListObjectParentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_object_parents_response.ListObjectParentsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_parents

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_parents.async_list_object_parents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_object_parents_request.ListObjectParentsRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level
        if include_all_links_to_each_parent is not None:
            input_["include_all_links_to_each_parent"] = (
                include_all_links_to_each_parent
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_object_policies(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_object_policies_response.ListObjectPoliciesResponse":
        """<p>Returns policies attached to an object in pagination fashion.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.</p>
            object_reference: <p>Reference that identifies the object for which policies will be listed.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
            consistency_level: <p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_object_policies_request.ListObjectPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_object_policies_response.ListObjectPoliciesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_policies

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_object_policies.async_list_object_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_object_policies_request.ListObjectPoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_outgoing_typed_links(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        filter_attribute_ranges: Optional[
            "aws_sdk_clouddirectory.types.typed_link_attribute_range_list.TypedLinkAttributeRangeList"
        ] = None,
        filter_typed_link: Optional[
            "aws_sdk_clouddirectory.types.typed_link_schema_and_facet_name.TypedLinkSchemaAndFacetName"
        ] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_outgoing_typed_links_response.ListOutgoingTypedLinksResponse":
        """<p>Returns a paginated list of all the outgoing <a>TypedLinkSpecifier</a> information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) of the directory where you want to list the typed links.</p>
            object_reference: <p>A reference that identifies the object whose attributes will be listed.</p>
            filter_attribute_ranges: <p>Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.</p>
            filter_typed_link: <p>Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
            consistency_level: <p>The consistency level to execute the request at.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_outgoing_typed_links_request.ListOutgoingTypedLinksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_outgoing_typed_links_response.ListOutgoingTypedLinksResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_outgoing_typed_links

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_outgoing_typed_links.async_list_outgoing_typed_links(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_outgoing_typed_links_request.ListOutgoingTypedLinksRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if filter_attribute_ranges is not None:
            input_["filter_attribute_ranges"] = filter_attribute_ranges
        if filter_typed_link is not None:
            input_["filter_typed_link"] = filter_typed_link
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_policy_attachments(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        policy_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
        consistency_level: Optional[
            "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse":
        """<p>Returns all of the <code>ObjectIdentifiers</code> to which a given policy is attached.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where objects reside. For more information, see <a>arns</a>.</p>
            policy_reference: <p>The reference that identifies the policy object.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
            consistency_level: <p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_policy_attachments_request.ListPolicyAttachmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_policy_attachments

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_policy_attachments.async_list_policy_attachments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_policy_attachments_request.ListPolicyAttachmentsRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["policy_reference"] = policy_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if consistency_level is not None:
            input_["consistency_level"] = consistency_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_published_schema_arns(
        self,
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        schema_arn: Optional["aws_sdk_clouddirectory.types.arn.Arn"] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_published_schema_arns_response.ListPublishedSchemaArnsResponse":
        """<p>Lists the major version families of each published schema. If a major version ARN is provided as <code>SchemaArn</code>, the minor version revisions in that family are listed instead.</p>

        Args:
            schema_arn: <p>The response for <code>ListPublishedSchemaArns</code> when this parameter is used will list all minor version ARNs for a major version.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_published_schema_arns_request.ListPublishedSchemaArnsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_published_schema_arns_response.ListPublishedSchemaArnsResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_published_schema_arns

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_published_schema_arns.async_list_published_schema_arns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_published_schema_arns_request.ListPublishedSchemaArnsRequest = {}  # type: ignore[typeddict-item]
        if schema_arn is not None:
            input_["schema_arn"] = schema_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.tags_number_results.TagsNumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns tags for a resource. Tagging is currently supported only for directories with a limit of 50 tags per directory. All 50 tags are returned for a given directory with this API call.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.</p>
            next_token: <p>The pagination token. This is for future use. Currently pagination is not supported for tagging.</p>
            max_results: <p>The <code>MaxResults</code> parameter sets the maximum number of results returned in a single page. This is for future use and is not supported currently.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_typed_link_facet_attributes(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_typed_link_facet_attributes_response.ListTypedLinkFacetAttributesResponse":
        """<p>Returns a paginated list of all attribute definitions for a particular <a>TypedLinkFacet</a>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>
            name: <p>The unique name of the typed link facet.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_typed_link_facet_attributes_request.ListTypedLinkFacetAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_typed_link_facet_attributes_response.ListTypedLinkFacetAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_typed_link_facet_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_typed_link_facet_attributes.async_list_typed_link_facet_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_typed_link_facet_attributes_request.ListTypedLinkFacetAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_typed_link_facet_names(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.list_typed_link_facet_names_response.ListTypedLinkFacetNamesResponse":
        """<p>Returns a paginated list of <code>TypedLink</code> facet names for a particular schema. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum number of results to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.list_typed_link_facet_names_request.ListTypedLinkFacetNamesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.list_typed_link_facet_names_response.ListTypedLinkFacetNamesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_typed_link_facet_names

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.list_typed_link_facet_names.async_list_typed_link_facet_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.list_typed_link_facet_names_request.ListTypedLinkFacetNamesRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def lookup_policy(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_clouddirectory.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_clouddirectory.types.number_results.NumberResults"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.lookup_policy_response.LookupPolicyResponse":
        """<p>Lists all policies from the root of the <a>Directory</a> to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects don't have the policies attached, it returns the <code>ObjectIdentifier</code> for such objects. If policies are present, it returns <code>ObjectIdentifier</code>, <code>policyId</code>, and <code>policyType</code>. Paths that don't lead to the root from the target object are ignored. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies\">Policies</a>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>
            object_reference: <p>Reference that identifies the object whose policies will be looked up.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of items to be retrieved in a single call. This is an approximate number.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.lookup_policy_request.LookupPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.lookup_policy_response.LookupPolicyResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.lookup_policy

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.lookup_policy.async_lookup_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.lookup_policy_request.LookupPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def publish_schema(
        self,
        development_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        version: "aws_sdk_clouddirectory.types.version.Version",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        minor_version: Optional["aws_sdk_clouddirectory.types.version.Version"] = None,
        name: Optional["aws_sdk_clouddirectory.types.schema_name.SchemaName"] = None,
    ) -> "aws_sdk_clouddirectory.types.publish_schema_response.PublishSchemaResponse":
        """<p>Publishes a development schema with a major version and a recommended minor version.</p>

        Args:
            development_schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the development schema. For more information, see <a>arns</a>.</p>
            version: <p>The major version under which the schema will be published. Schemas have both a major and minor version associated with them.</p>
            minor_version: <p>The minor version under which the schema will be published. This parameter is recommended. Schemas have both a major and minor version associated with them.</p>
            name: <p>The new name under which the schema will be published. If this is not provided, the development schema is considered.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.publish_schema_request.PublishSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.publish_schema_response.PublishSchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.publish_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.publish_schema.async_publish_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.publish_schema_request.PublishSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["development_schema_arn"] = development_schema_arn
        input_["version"] = version
        if minor_version is not None:
            input_["minor_version"] = minor_version
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_schema_from_json(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        document: "aws_sdk_clouddirectory.types.schema_json_document.SchemaJsonDocument",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.put_schema_from_json_response.PutSchemaFromJsonResponse":
        """<p>Allows a schema to be updated using JSON upload. Only available for development schemas. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_jsonformat.html#schemas_json\">JSON Schema Format</a> for more information.</p>

        Args:
            schema_arn: <p>The ARN of the schema to update.</p>
            document: <p>The replacement JSON schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.put_schema_from_json_request.PutSchemaFromJsonRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.put_schema_from_json_response.PutSchemaFromJsonResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.put_schema_from_json

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.put_schema_from_json.async_put_schema_from_json(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.put_schema_from_json_request.PutSchemaFromJsonRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["document"] = document

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_facet_from_object(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        schema_facet: "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.remove_facet_from_object_response.RemoveFacetFromObjectResponse":
        """<p>Removes the specified facet from the specified object.</p>

        Args:
            directory_arn: <p>The ARN of the directory in which the object resides.</p>
            schema_facet: <p>The facet to remove. See <a>SchemaFacet</a> for details.</p>
            object_reference: <p>A reference to the object to remove the facet from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.remove_facet_from_object_request.RemoveFacetFromObjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.remove_facet_from_object_response.RemoveFacetFromObjectResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.remove_facet_from_object

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.remove_facet_from_object.async_remove_facet_from_object(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.remove_facet_from_object_request.RemoveFacetFromObjectRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["schema_facet"] = schema_facet
        input_["object_reference"] = object_reference

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        tags: "aws_sdk_clouddirectory.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.tag_resource_response.TagResourceResponse":
        """<p>An API operation for adding tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.</p>
            tags: <p>A list of tag key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        tag_keys: "aws_sdk_clouddirectory.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.untag_resource_response.UntagResourceResponse":
        """<p>An API operation for removing tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.</p>
            tag_keys: <p>Keys of the tag that need to be removed from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.facet_name.FacetName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        attribute_updates: Optional[
            "aws_sdk_clouddirectory.types.facet_attribute_update_list.FacetAttributeUpdateList"
        ] = None,
        object_type: Optional[
            "aws_sdk_clouddirectory.types.object_type.ObjectType"
        ] = None,
    ) -> "aws_sdk_clouddirectory.types.update_facet_response.UpdateFacetResponse":
        """<p>Does the following:</p> <ol> <li> <p>Adds new <code>Attributes</code>, <code>Rules</code>, or <code>ObjectTypes</code>.</p> </li> <li> <p>Updates existing <code>Attributes</code>, <code>Rules</code>, or <code>ObjectTypes</code>.</p> </li> <li> <p>Deletes existing <code>Attributes</code>, <code>Rules</code>, or <code>ObjectTypes</code>.</p> </li> </ol>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>
            name: <p>The name of the facet.</p>
            attribute_updates: <p>List of attributes that need to be updated in a given schema <a>Facet</a>. Each attribute is followed by <code>AttributeAction</code>, which specifies the type of update operation to perform. </p>
            object_type: <p>The object type that is associated with the facet. See <a>CreateFacetRequest$ObjectType</a> for more details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.update_facet_request.UpdateFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.update_facet_response.UpdateFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_facet.async_update_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.update_facet_request.UpdateFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name
        if attribute_updates is not None:
            input_["attribute_updates"] = attribute_updates
        if object_type is not None:
            input_["object_type"] = object_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_link_attributes(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        typed_link_specifier: "aws_sdk_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier",
        attribute_updates: "aws_sdk_clouddirectory.types.link_attribute_update_list.LinkAttributeUpdateList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.update_link_attributes_response.UpdateLinkAttributesResponse":
        """<p>Updates a given typed link’s attributes. Attributes to be updated must not contribute to the typed link’s identity, as defined by its <code>IdentityAttributeOrder</code>.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the Directory where the updated typed link resides. For more information, see <a>arns</a> or <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>
            typed_link_specifier: <p>Allows a typed link specifier to be accepted as input.</p>
            attribute_updates: <p>The attributes update structure.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.update_link_attributes_request.UpdateLinkAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.update_link_attributes_response.UpdateLinkAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_link_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_link_attributes.async_update_link_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.update_link_attributes_request.UpdateLinkAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["typed_link_specifier"] = typed_link_specifier
        input_["attribute_updates"] = attribute_updates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_object_attributes(
        self,
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference",
        attribute_updates: "aws_sdk_clouddirectory.types.object_attribute_update_list.ObjectAttributeUpdateList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.update_object_attributes_response.UpdateObjectAttributesResponse":
        """<p>Updates a given object's attributes.</p>

        Args:
            directory_arn: <p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>
            object_reference: <p>The reference that identifies the object.</p>
            attribute_updates: <p>The attributes update structure.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.update_object_attributes_request.UpdateObjectAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.update_object_attributes_response.UpdateObjectAttributesResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_object_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_object_attributes.async_update_object_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.update_object_attributes_request.UpdateObjectAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["directory_arn"] = directory_arn
        input_["object_reference"] = object_reference
        input_["attribute_updates"] = attribute_updates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_schema(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.schema_name.SchemaName",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.update_schema_response.UpdateSchemaResponse":
        """<p>Updates the schema name with a new name. Only development schema names can be updated.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.</p>
            name: <p>The name of the schema.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.update_schema_request.UpdateSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.update_schema_response.UpdateSchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_schema.async_update_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.update_schema_request.UpdateSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_typed_link_facet(
        self,
        schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName",
        attribute_updates: "aws_sdk_clouddirectory.types.typed_link_facet_attribute_update_list.TypedLinkFacetAttributeUpdateList",
        identity_attribute_order: "aws_sdk_clouddirectory.types.attribute_name_list.AttributeNameList",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
    ) -> "aws_sdk_clouddirectory.types.update_typed_link_facet_response.UpdateTypedLinkFacetResponse":
        """<p>Updates a <a>TypedLinkFacet</a>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>

        Args:
            schema_arn: <p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>
            name: <p>The unique name of the typed link facet.</p>
            attribute_updates: <p>Attributes update structure.</p>
            identity_attribute_order: <p>The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to a typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink\">Typed Links</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.update_typed_link_facet_request.UpdateTypedLinkFacetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.update_typed_link_facet_response.UpdateTypedLinkFacetResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_typed_link_facet

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.update_typed_link_facet.async_update_typed_link_facet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.update_typed_link_facet_request.UpdateTypedLinkFacetRequest = {}  # type: ignore[typeddict-item]
        input_["schema_arn"] = schema_arn
        input_["name"] = name
        input_["attribute_updates"] = attribute_updates
        input_["identity_attribute_order"] = identity_attribute_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_applied_schema(
        self,
        published_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        directory_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        dry_run: Optional["aws_sdk_clouddirectory.types.bool.Bool"] = None,
    ) -> "aws_sdk_clouddirectory.types.upgrade_applied_schema_response.UpgradeAppliedSchemaResponse":
        """<p>Upgrades a single directory in-place using the <code>PublishedSchemaArn</code> with schema updates found in <code>MinorVersion</code>. Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory. Note: This is a synchronous API call and upgrades only one schema on a given directory per call. To upgrade multiple directories from one schema, you would need to call this API on each directory.</p>

        Args:
            published_schema_arn: <p>The revision of the published schema to upgrade the directory to.</p>
            directory_arn: <p>The ARN for the directory to which the upgraded schema will be applied.</p>
            dry_run: <p>Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.upgrade_applied_schema_request.UpgradeAppliedSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.upgrade_applied_schema_response.UpgradeAppliedSchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.upgrade_applied_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.upgrade_applied_schema.async_upgrade_applied_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.upgrade_applied_schema_request.UpgradeAppliedSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["published_schema_arn"] = published_schema_arn
        input_["directory_arn"] = directory_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_published_schema(
        self,
        development_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        published_schema_arn: "aws_sdk_clouddirectory.types.arn.Arn",
        minor_version: "aws_sdk_clouddirectory.types.version.Version",
        *,
        config_overrides: Optional[AsyncCloudDirectoryClientConfig] = None,
        dry_run: Optional["aws_sdk_clouddirectory.types.bool.Bool"] = None,
    ) -> "aws_sdk_clouddirectory.types.upgrade_published_schema_response.UpgradePublishedSchemaResponse":
        """<p>Upgrades a published schema under a new minor version revision using the current contents of <code>DevelopmentSchemaArn</code>.</p>

        Args:
            development_schema_arn: <p>The ARN of the development schema with the changes used for the upgrade.</p>
            published_schema_arn: <p>The ARN of the published schema to be upgraded.</p>
            minor_version: <p>Identifies the minor version of the published schema that will be created. This parameter is NOT optional.</p>
            dry_run: <p>Used for testing whether the Development schema provided is backwards compatible, or not, with the publish schema provided by the user to be upgraded. If schema compatibility fails, an exception would be thrown else the call would succeed. This parameter is optional and defaults to false.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_clouddirectory.types.upgrade_published_schema_request.UpgradePublishedSchemaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_clouddirectory.types.upgrade_published_schema_response.UpgradePublishedSchemaResponse"
        ]:
            import aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.upgrade_published_schema

            (
                output,
                http_response,
            ) = await aws_sdk_clouddirectory._operations.amazon_cloud_directory_20170111.upgrade_published_schema.async_upgrade_published_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_clouddirectory.types.upgrade_published_schema_request.UpgradePublishedSchemaRequest = {}  # type: ignore[typeddict-item]
        input_["development_schema_arn"] = development_schema_arn
        input_["published_schema_arn"] = published_schema_arn
        input_["minor_version"] = minor_version
        if dry_run is not None:
            input_["dry_run"] = dry_run

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
