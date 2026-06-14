"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AWS242AppRegistry``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_service_catalog_appregistry._auth._signers
import aws_sdk_service_catalog_appregistry._auth._sigv4
from aws_sdk_service_catalog_appregistry._auth._identity import Credentials
from aws_sdk_service_catalog_appregistry._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_service_catalog_appregistry._auth._zapros_handler import AuthMiddleware
from aws_sdk_service_catalog_appregistry._pagination import (
    resolve_path as _resolve_path,
)
from aws_sdk_service_catalog_appregistry._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.app_registry_configuration
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.application_summary
    import aws_sdk_service_catalog_appregistry.types.arn
    import aws_sdk_service_catalog_appregistry.types.associate_attribute_group_request
    import aws_sdk_service_catalog_appregistry.types.associate_attribute_group_response
    import aws_sdk_service_catalog_appregistry.types.associate_resource_request
    import aws_sdk_service_catalog_appregistry.types.associate_resource_response
    import aws_sdk_service_catalog_appregistry.types.attribute_group_details
    import aws_sdk_service_catalog_appregistry.types.attribute_group_id
    import aws_sdk_service_catalog_appregistry.types.attribute_group_specifier
    import aws_sdk_service_catalog_appregistry.types.attribute_group_summary
    import aws_sdk_service_catalog_appregistry.types.attributes
    import aws_sdk_service_catalog_appregistry.types.client_token
    import aws_sdk_service_catalog_appregistry.types.create_application_request
    import aws_sdk_service_catalog_appregistry.types.create_application_response
    import aws_sdk_service_catalog_appregistry.types.create_attribute_group_request
    import aws_sdk_service_catalog_appregistry.types.create_attribute_group_response
    import aws_sdk_service_catalog_appregistry.types.delete_application_request
    import aws_sdk_service_catalog_appregistry.types.delete_application_response
    import aws_sdk_service_catalog_appregistry.types.delete_attribute_group_request
    import aws_sdk_service_catalog_appregistry.types.delete_attribute_group_response
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.disassociate_attribute_group_request
    import aws_sdk_service_catalog_appregistry.types.disassociate_attribute_group_response
    import aws_sdk_service_catalog_appregistry.types.disassociate_resource_request
    import aws_sdk_service_catalog_appregistry.types.disassociate_resource_response
    import aws_sdk_service_catalog_appregistry.types.get_application_request
    import aws_sdk_service_catalog_appregistry.types.get_application_response
    import aws_sdk_service_catalog_appregistry.types.get_associated_resource_filter
    import aws_sdk_service_catalog_appregistry.types.get_associated_resource_request
    import aws_sdk_service_catalog_appregistry.types.get_associated_resource_response
    import aws_sdk_service_catalog_appregistry.types.get_attribute_group_request
    import aws_sdk_service_catalog_appregistry.types.get_attribute_group_response
    import aws_sdk_service_catalog_appregistry.types.get_configuration_response
    import aws_sdk_service_catalog_appregistry.types.list_applications_request
    import aws_sdk_service_catalog_appregistry.types.list_applications_response
    import aws_sdk_service_catalog_appregistry.types.list_associated_attribute_groups_request
    import aws_sdk_service_catalog_appregistry.types.list_associated_attribute_groups_response
    import aws_sdk_service_catalog_appregistry.types.list_associated_resources_request
    import aws_sdk_service_catalog_appregistry.types.list_associated_resources_response
    import aws_sdk_service_catalog_appregistry.types.list_attribute_groups_for_application_request
    import aws_sdk_service_catalog_appregistry.types.list_attribute_groups_for_application_response
    import aws_sdk_service_catalog_appregistry.types.list_attribute_groups_request
    import aws_sdk_service_catalog_appregistry.types.list_attribute_groups_response
    import aws_sdk_service_catalog_appregistry.types.list_tags_for_resource_request
    import aws_sdk_service_catalog_appregistry.types.list_tags_for_resource_response
    import aws_sdk_service_catalog_appregistry.types.max_results
    import aws_sdk_service_catalog_appregistry.types.name
    import aws_sdk_service_catalog_appregistry.types.next_token
    import aws_sdk_service_catalog_appregistry.types.options
    import aws_sdk_service_catalog_appregistry.types.put_configuration_request
    import aws_sdk_service_catalog_appregistry.types.resource_info
    import aws_sdk_service_catalog_appregistry.types.resource_specifier
    import aws_sdk_service_catalog_appregistry.types.resource_type
    import aws_sdk_service_catalog_appregistry.types.sync_resource_request
    import aws_sdk_service_catalog_appregistry.types.sync_resource_response
    import aws_sdk_service_catalog_appregistry.types.tag_keys
    import aws_sdk_service_catalog_appregistry.types.tag_resource_request
    import aws_sdk_service_catalog_appregistry.types.tag_resource_response
    import aws_sdk_service_catalog_appregistry.types.tags
    import aws_sdk_service_catalog_appregistry.types.untag_resource_request
    import aws_sdk_service_catalog_appregistry.types.untag_resource_response
    import aws_sdk_service_catalog_appregistry.types.update_application_request
    import aws_sdk_service_catalog_appregistry.types.update_application_response
    import aws_sdk_service_catalog_appregistry.types.update_attribute_group_request
    import aws_sdk_service_catalog_appregistry.types.update_attribute_group_response


class ServiceCatalogAppRegistryClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class ServiceCatalogAppRegistryClient:
    """A client for the ``ServiceCatalogAppRegistry`` service.

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
        self._config = ServiceCatalogAppRegistryClientConfig(
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
        self, config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ServiceCatalogAppRegistryClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    def associate_attribute_group(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.associate_attribute_group_response.AssociateAttributeGroupResponse":
        """<p>Associates an attribute group with an application to augment the application's metadata with the group's attributes. This feature enables applications to be described with user-defined details that are machine-readable, such as third-party integrations.</p>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
            attribute_group: <p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.associate_attribute_group_request.AssociateAttributeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.associate_attribute_group_response.AssociateAttributeGroupResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.associate_attribute_group

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.associate_attribute_group.associate_attribute_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.associate_attribute_group_request.AssociateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
        input_["attribute_group"] = attribute_group

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_resource(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        resource_type: "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType",
        resource: "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        options: Optional[
            "aws_sdk_service_catalog_appregistry.types.options.Options"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.associate_resource_response.AssociateResourceResponse":
        """<p> Associates a resource with an application. The resource can be specified by its ARN or name. The application can be specified by ARN, ID, or name. </p> <p> <b>Minimum permissions</b> </p> <p> You must have the following permissions to associate a resource using the <code>OPTIONS</code> parameter set to <code>APPLY_APPLICATION_TAG</code>. </p> <ul> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>tag:TagResources</code> </p> </li> </ul> <p> You must also have these additional permissions if you don't use the <code>AWSServiceCatalogAppRegistryFullAccess</code> policy. For more information, see <a href=\"https://docs.aws.amazon.com/servicecatalog/latest/arguide/full.html\">AWSServiceCatalogAppRegistryFullAccess</a> in the AppRegistry Administrator Guide. </p> <ul> <li> <p> <code>resource-groups:AssociateResource</code> </p> </li> <li> <p> <code>cloudformation:UpdateStack</code> </p> </li> <li> <p> <code>cloudformation:DescribeStacks</code> </p> </li> </ul> <note> <p> In addition, you must have the tagging permission defined by the Amazon Web Services service that creates the resource. For more information, see <a href=\"https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html\">TagResources</a> in the <i>Resource Groups Tagging API Reference</i>. </p> </note>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
            resource_type: <p>The type of resource of which the application will be associated.</p>
            resource: <p>The name or ID of the resource of which the application will be associated.</p>
            options: <p> Determines whether an application tag is applied or skipped. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.associate_resource_request.AssociateResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.associate_resource_response.AssociateResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.associate_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.associate_resource.associate_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.associate_resource_request.AssociateResourceRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
        input_["resource_type"] = resource_type
        input_["resource"] = resource
        if options is not None:
            input_["options"] = options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_application(
        self,
        name: "aws_sdk_service_catalog_appregistry.types.name.Name",
        client_token: "aws_sdk_service_catalog_appregistry.types.client_token.ClientToken",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        description: Optional[
            "aws_sdk_service_catalog_appregistry.types.description.Description"
        ] = None,
        tags: Optional["aws_sdk_service_catalog_appregistry.types.tags.Tags"] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.create_application_response.CreateApplicationResponse":
        """<p>Creates a new application that is the top-level node in a hierarchy of related cloud resource abstractions.</p>

        Args:
            name: <p>The name of the application. The name must be unique in the region in which you are creating the application.</p>
            description: <p>The description of the application.</p>
            tags: <p>Key-value pairs you can use to associate with the application.</p>
            client_token: <p>A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.create_application_response.CreateApplicationResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.create_application

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_attribute_group(
        self,
        name: "aws_sdk_service_catalog_appregistry.types.name.Name",
        attributes: "aws_sdk_service_catalog_appregistry.types.attributes.Attributes",
        client_token: "aws_sdk_service_catalog_appregistry.types.client_token.ClientToken",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        description: Optional[
            "aws_sdk_service_catalog_appregistry.types.description.Description"
        ] = None,
        tags: Optional["aws_sdk_service_catalog_appregistry.types.tags.Tags"] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.create_attribute_group_response.CreateAttributeGroupResponse":
        """<p>Creates a new attribute group as a container for user-defined attributes. This feature enables users to have full control over their cloud application's metadata in a rich machine-readable format to facilitate integration with automated workflows and third-party tools.</p>

        Args:
            name: <p>The name of the attribute group.</p>
            description: <p>The description of the attribute group that the user provides.</p>
            attributes: <p>A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.</p>
            tags: <p>Key-value pairs you can use to associate with the attribute group.</p>
            client_token: <p>A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.create_attribute_group_request.CreateAttributeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.create_attribute_group_response.CreateAttributeGroupResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.create_attribute_group

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.create_attribute_group.create_attribute_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.create_attribute_group_request.CreateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["attributes"] = attributes
        if tags is not None:
            input_["tags"] = tags
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_application(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an application that is specified either by its application ID, name, or ARN. All associated attribute groups and resources must be disassociated from it before deleting an application.</p>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.delete_application

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_attribute_group(
        self,
        attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.delete_attribute_group_response.DeleteAttributeGroupResponse":
        """<p>Deletes an attribute group, specified either by its attribute group ID, name, or ARN.</p>

        Args:
            attribute_group: <p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.delete_attribute_group_request.DeleteAttributeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.delete_attribute_group_response.DeleteAttributeGroupResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.delete_attribute_group

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.delete_attribute_group.delete_attribute_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.delete_attribute_group_request.DeleteAttributeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["attribute_group"] = attribute_group

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_attribute_group(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.disassociate_attribute_group_response.DisassociateAttributeGroupResponse":
        """<p>Disassociates an attribute group from an application to remove the extra attributes contained in the attribute group from the application's metadata. This operation reverts <code>AssociateAttributeGroup</code>.</p>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
            attribute_group: <p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.disassociate_attribute_group_request.DisassociateAttributeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.disassociate_attribute_group_response.DisassociateAttributeGroupResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.disassociate_attribute_group

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.disassociate_attribute_group.disassociate_attribute_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.disassociate_attribute_group_request.DisassociateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
        input_["attribute_group"] = attribute_group

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_resource(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        resource_type: "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType",
        resource: "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.disassociate_resource_response.DisassociateResourceResponse":
        """<p> Disassociates a resource from application. Both the resource and the application can be specified either by ID or name. </p> <p> <b>Minimum permissions</b> </p> <p> You must have the following permissions to remove a resource that's been associated with an application using the <code>APPLY_APPLICATION_TAG</code> option for <a href=\"https://docs.aws.amazon.com/servicecatalog/latest/dg/API_app-registry_AssociateResource.html\">AssociateResource</a>. </p> <ul> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>tag:UntagResources</code> </p> </li> </ul> <p> You must also have the following permissions if you don't use the <code>AWSServiceCatalogAppRegistryFullAccess</code> policy. For more information, see <a href=\"https://docs.aws.amazon.com/servicecatalog/latest/arguide/full.html\">AWSServiceCatalogAppRegistryFullAccess</a> in the AppRegistry Administrator Guide. </p> <ul> <li> <p> <code>resource-groups:DisassociateResource</code> </p> </li> <li> <p> <code>cloudformation:UpdateStack</code> </p> </li> <li> <p> <code>cloudformation:DescribeStacks</code> </p> </li> </ul> <note> <p> In addition, you must have the tagging permission defined by the Amazon Web Services service that creates the resource. For more information, see <a href=\"https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntTagResources.html\">UntagResources</a> in the <i>Resource Groups Tagging API Reference</i>. </p> </note>

        Args:
            application: <p>The name or ID of the application.</p>
            resource_type: <p>The type of the resource that is being disassociated.</p>
            resource: <p>The name or ID of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.disassociate_resource_request.DisassociateResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.disassociate_resource_response.DisassociateResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.disassociate_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.disassociate_resource.disassociate_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.disassociate_resource_request.DisassociateResourceRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
        input_["resource_type"] = resource_type
        input_["resource"] = resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_application(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.get_application_response.GetApplicationResponse":
        """<p> Retrieves metadata information about one of your applications. The application can be specified by its ARN, ID, or name (which is unique within one account in one region at a given point in time). Specify by ARN or ID in automated workflows if you want to make sure that the exact same application is returned or a <code>ResourceNotFoundException</code> is thrown, avoiding the ABA addressing problem. </p>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.get_application_response.GetApplicationResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_application

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.get_application_request.GetApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_associated_resource(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        resource_type: "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType",
        resource: "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        resource_tag_status: Optional[
            "aws_sdk_service_catalog_appregistry.types.get_associated_resource_filter.GetAssociatedResourceFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.get_associated_resource_response.GetAssociatedResourceResponse":
        """<p>Gets the resource associated with the application.</p>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
            resource_type: <p>The type of resource associated with the application.</p>
            resource: <p>The name or ID of the resource associated with the application.</p>
            next_token: <p> A unique pagination token for each page of results. Make the call again with the returned token to retrieve the next page of results. </p>
            resource_tag_status: <p> States whether an application tag is applied, not applied, in the process of being applied, or skipped. </p>
            max_results: <p> The maximum number of results to return. If the parameter is omitted, it defaults to 25. The value is optional. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.get_associated_resource_request.GetAssociatedResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.get_associated_resource_response.GetAssociatedResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_associated_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_associated_resource.get_associated_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.get_associated_resource_request.GetAssociatedResourceRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
        input_["resource_type"] = resource_type
        input_["resource"] = resource
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_tag_status is not None:
            input_["resource_tag_status"] = resource_tag_status
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_attribute_group(
        self,
        attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.get_attribute_group_response.GetAttributeGroupResponse":
        """<p> Retrieves an attribute group by its ARN, ID, or name. The attribute group can be specified by its ARN, ID, or name. </p>

        Args:
            attribute_group: <p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.get_attribute_group_request.GetAttributeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.get_attribute_group_response.GetAttributeGroupResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_attribute_group

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_attribute_group.get_attribute_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.get_attribute_group_request.GetAttributeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["attribute_group"] = attribute_group

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_configuration(
        self,
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.get_configuration_response.GetConfigurationResponse":
        """<p> Retrieves a <code>TagKey</code> configuration from an account. </p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_configuration

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.get_configuration.get_configuration(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_applications(
        self,
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves a list of all of your applications. Results are paginated.</p>

        Args:
            next_token: <p>The token to use to get the next page of results after a previous API call. </p>
            max_results: <p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_applications

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_service_catalog_appregistry.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_associated_attribute_groups(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.list_associated_attribute_groups_response.ListAssociatedAttributeGroupsResponse":
        """<p>Lists all attribute groups that are associated with specified application. Results are paginated.</p>

        Args:
            application: <p>The name or ID of the application.</p>
            next_token: <p>The token to use to get the next page of results after a previous API call. </p>
            max_results: <p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.list_associated_attribute_groups_request.ListAssociatedAttributeGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.list_associated_attribute_groups_response.ListAssociatedAttributeGroupsResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_associated_attribute_groups

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_associated_attribute_groups.list_associated_attribute_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.list_associated_attribute_groups_request.ListAssociatedAttributeGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
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

    def iter_list_associated_attribute_groups(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_service_catalog_appregistry.types.attribute_group_id.AttributeGroupId]":
        _token = next_token
        while True:
            _response = self.list_associated_attribute_groups(
                application,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attribute_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_associated_resources(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.list_associated_resources_response.ListAssociatedResourcesResponse":
        """<p> Lists all of the resources that are associated with the specified application. Results are paginated. </p> <note> <p> If you share an application, and a consumer account associates a tag query to the application, all of the users who can access the application can also view the tag values in all accounts that are associated with it using this API. </p> </note>

        Args:
            application: <p> The name, ID, or ARN of the application. </p>
            next_token: <p>The token to use to get the next page of results after a previous API call. </p>
            max_results: <p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.list_associated_resources_request.ListAssociatedResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.list_associated_resources_response.ListAssociatedResourcesResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_associated_resources

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_associated_resources.list_associated_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.list_associated_resources_request.ListAssociatedResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
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

    def iter_list_associated_resources(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "Iterator[aws_sdk_service_catalog_appregistry.types.resource_info.ResourceInfo]"
    ):
        _token = next_token
        while True:
            _response = self.list_associated_resources(
                application,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_attribute_groups(
        self,
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.list_attribute_groups_response.ListAttributeGroupsResponse":
        """<p>Lists all attribute groups which you have access to. Results are paginated.</p>

        Args:
            next_token: <p>The token to use to get the next page of results after a previous API call. </p>
            max_results: <p>The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.list_attribute_groups_request.ListAttributeGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.list_attribute_groups_response.ListAttributeGroupsResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_attribute_groups

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_attribute_groups.list_attribute_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.list_attribute_groups_request.ListAttributeGroupsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_attribute_groups(
        self,
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_service_catalog_appregistry.types.attribute_group_summary.AttributeGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_attribute_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attribute_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_attribute_groups_for_application(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.list_attribute_groups_for_application_response.ListAttributeGroupsForApplicationResponse":
        """<p>Lists the details of all attribute groups associated with a specific application. The results display in pages.</p>

        Args:
            application: <p>The name or ID of the application.</p>
            next_token: <p>This token retrieves the next page of results after a previous API call.</p>
            max_results: <p>The upper bound of the number of results to return. The value cannot exceed 25. If you omit this parameter, it defaults to 25. This value is optional.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.list_attribute_groups_for_application_request.ListAttributeGroupsForApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.list_attribute_groups_for_application_response.ListAttributeGroupsForApplicationResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_attribute_groups_for_application

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_attribute_groups_for_application.list_attribute_groups_for_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.list_attribute_groups_for_application_request.ListAttributeGroupsForApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
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

    def iter_list_attribute_groups_for_application(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        next_token: Optional[
            "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_service_catalog_appregistry.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_service_catalog_appregistry.types.attribute_group_details.AttributeGroupDetails]":
        _token = next_token
        while True:
            _response = self.list_attribute_groups_for_application(
                application,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attribute_groups_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_service_catalog_appregistry.types.arn.Arn",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags on the resource.</p>

        Args:
            resource_arn: <p>The Amazon resource name (ARN) that specifies the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_tags_for_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_configuration(
        self,
        configuration: "aws_sdk_service_catalog_appregistry.types.app_registry_configuration.AppRegistryConfiguration",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> None:
        """<p> Associates a <code>TagKey</code> configuration to an account. </p>

        Args:
            configuration: <p> Associates a <code>TagKey</code> configuration to an account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.put_configuration_request.PutConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.put_configuration

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.put_configuration.put_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.put_configuration_request.PutConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def sync_resource(
        self,
        resource_type: "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType",
        resource: "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.sync_resource_response.SyncResourceResponse":
        """<p>Syncs the resource with current AppRegistry records.</p> <p>Specifically, the resource’s AppRegistry system tags sync with its associated application. We remove the resource's AppRegistry system tags if it does not associate with the application. The caller must have permissions to read and update the resource.</p>

        Args:
            resource_type: <p>The type of resource of which the application will be associated.</p>
            resource: <p>An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an Amazon Web Services CloudFormation stack, or an Amazon S3 bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.sync_resource_request.SyncResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.sync_resource_response.SyncResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.sync_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.sync_resource.sync_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.sync_resource_request.SyncResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_type"] = resource_type
        input_["resource"] = resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_service_catalog_appregistry.types.arn.Arn",
        tags: "aws_sdk_service_catalog_appregistry.types.tags.Tags",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p> <p>Each tag consists of a key and an optional value. If a tag with the same key is already associated with the resource, this action updates its value.</p> <p>This operation returns an empty response if the call was successful.</p>

        Args:
            resource_arn: <p>The Amazon resource name (ARN) that specifies the resource.</p>
            tags: <p>The new or modified tags for the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.tag_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_service_catalog_appregistry.types.arn.Arn",
        tag_keys: "aws_sdk_service_catalog_appregistry.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p> <p>This operation returns an empty response if the call was successful.</p>

        Args:
            resource_arn: <p>The Amazon resource name (ARN) that specifies the resource.</p>
            tag_keys: <p>A list of the tag keys to remove from the specified resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.untag_resource

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_application(
        self,
        application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        name: Optional["aws_sdk_service_catalog_appregistry.types.name.Name"] = None,
        description: Optional[
            "aws_sdk_service_catalog_appregistry.types.description.Description"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an existing application with new attributes.</p>

        Args:
            application: <p> The name, ID, or ARN of the application that will be updated. </p>
            name: <p>Deprecated: The new name of the application. The name must be unique in the region in which you are updating the application. Please do not use this field as we have stopped supporting name updates.</p>
            description: <p>The new description of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.update_application_response.UpdateApplicationResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.update_application

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application"] = application
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_attribute_group(
        self,
        attribute_group: "aws_sdk_service_catalog_appregistry.types.attribute_group_specifier.AttributeGroupSpecifier",
        *,
        config_overrides: Optional[ServiceCatalogAppRegistryClientConfig] = None,
        name: Optional["aws_sdk_service_catalog_appregistry.types.name.Name"] = None,
        description: Optional[
            "aws_sdk_service_catalog_appregistry.types.description.Description"
        ] = None,
        attributes: Optional[
            "aws_sdk_service_catalog_appregistry.types.attributes.Attributes"
        ] = None,
    ) -> "aws_sdk_service_catalog_appregistry.types.update_attribute_group_response.UpdateAttributeGroupResponse":
        """<p>Updates an existing attribute group with new details. </p>

        Args:
            attribute_group: <p> The name, ID, or ARN of the attribute group that holds the attributes to describe the application. </p>
            name: <p>Deprecated: The new name of the attribute group. The name must be unique in the region in which you are updating the attribute group. Please do not use this field as we have stopped supporting name updates.</p>
            description: <p>The description of the attribute group that the user provides.</p>
            attributes: <p>A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_service_catalog_appregistry.types.update_attribute_group_request.UpdateAttributeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_service_catalog_appregistry.types.update_attribute_group_response.UpdateAttributeGroupResponse"
        ]:
            import aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.update_attribute_group

            output, http_response = (
                aws_sdk_service_catalog_appregistry._operations.aws242_app_registry.update_attribute_group.update_attribute_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_service_catalog_appregistry.types.update_attribute_group_request.UpdateAttributeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["attribute_group"] = attribute_group
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

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
