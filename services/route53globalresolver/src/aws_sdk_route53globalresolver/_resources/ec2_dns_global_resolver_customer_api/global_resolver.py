from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_route53globalresolver._auth._signers
import aws_sdk_route53globalresolver._auth._sigv4
from aws_sdk_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.create_global_resolver_input
    import aws_sdk_route53globalresolver.types.create_global_resolver_output
    import aws_sdk_route53globalresolver.types.delete_global_resolver_input
    import aws_sdk_route53globalresolver.types.delete_global_resolver_output
    import aws_sdk_route53globalresolver.types.get_global_resolver_input
    import aws_sdk_route53globalresolver.types.get_global_resolver_output
    import aws_sdk_route53globalresolver.types.global_resolver_ip_address_type
    import aws_sdk_route53globalresolver.types.global_resolvers_item
    import aws_sdk_route53globalresolver.types.list_global_resolvers_input
    import aws_sdk_route53globalresolver.types.list_global_resolvers_output
    import aws_sdk_route53globalresolver.types.region
    import aws_sdk_route53globalresolver.types.regions
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.tags
    import aws_sdk_route53globalresolver.types.update_global_resolver_input
    import aws_sdk_route53globalresolver.types.update_global_resolver_output
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class GlobalResolver:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        regions: "aws_sdk_route53globalresolver.types.regions.Regions",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
        ] = None,
        observability_region: Optional[
            "aws_sdk_route53globalresolver.types.region.Region"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_global_resolver_output.CreateGlobalResolverOutput":
        """<p>Creates a new Route 53 Global Resolver instance. A Route 53 Global Resolver is a global, internet-accessible DNS resolver that provides secure DNS resolution for both public and private domains through global anycast IP addresses.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique string that identifies the request and ensures idempotency. If you make multiple requests with the same client token, only one Route 53 Global Resolver is created.</p>
            description: <p>An optional description for the Route 53 Global Resolver instance. Maximum length of 1024 characters.</p>
            ip_address_type: <p>The IP address type for the Route 53 Global Resolver. Valid values are IPV4 (default) or DUAL_STACK for both IPv4 and IPv6 support.</p>
            name: <p>A descriptive name for the Route 53 Global Resolver instance. Maximum length of 64 characters.</p>
            observability_region: <p>The Amazon Web Services Region where query resolution logs and metrics will be aggregated and delivered. If not specified, logging is not enabled.</p>
            regions: <p>List of Amazon Web Services Regions where the Route 53 Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>
            tags: <p>Tags to associate with the Route 53 Global Resolver. Tags are key-value pairs that help you organize and identify your resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.create_global_resolver_input.CreateGlobalResolverInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.create_global_resolver_output.CreateGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_global_resolver

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_global_resolver.create_global_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.create_global_resolver_input.CreateGlobalResolverInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        input_["name"] = name
        if observability_region is not None:
            input_["observability_region"] = observability_region
        input_["regions"] = regions
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_global_resolver_output.GetGlobalResolverOutput":
        """<p>Retrieves information about a Route 53 Global Resolver instance.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_global_resolver_input.GetGlobalResolverInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_global_resolver_output.GetGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_global_resolver

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_global_resolver.get_global_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_global_resolver_input.GetGlobalResolverInput = {}  # type: ignore[typeddict-item]
        input_["global_resolver_id"] = global_resolver_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        observability_region: Optional[
            "aws_sdk_route53globalresolver.types.region.Region"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
        ] = None,
        regions: Optional["aws_sdk_route53globalresolver.types.regions.Regions"] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_global_resolver_output.UpdateGlobalResolverOutput":
        """<p>Updates the configuration of a Route 53 Global Resolver instance. You can modify the name, description, and observability Region.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Global Resolver.</p>
            name: <p>The name of the Global Resolver.</p>
            observability_region: <p>The Amazon Web Services Regions in which the users' Global Resolver query resolution logs will be propagated.</p>
            description: <p>The description of the Global Resolver.</p>
            ip_address_type: <p>The IP address type for the Global Resolver. Valid values are IPV4 or DUAL_STACK for both IPv4 and IPv6 support.</p>
            regions: <p>The list of Amazon Web Services Regions where the Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.update_global_resolver_input.UpdateGlobalResolverInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.update_global_resolver_output.UpdateGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_global_resolver

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_global_resolver.update_global_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.update_global_resolver_input.UpdateGlobalResolverInput = {}  # type: ignore[typeddict-item]
        input_["global_resolver_id"] = global_resolver_id
        if name is not None:
            input_["name"] = name
        if observability_region is not None:
            input_["observability_region"] = observability_region
        if description is not None:
            input_["description"] = description
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if regions is not None:
            input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_global_resolver_output.DeleteGlobalResolverOutput":
        """<p>Deletes a Route 53 Global Resolver instance. This operation cannot be undone. All associated DNS views, access sources, tokens, and firewall rules are also deleted.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The unique identifier of the Route 53 Global Resolver to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.delete_global_resolver_input.DeleteGlobalResolverInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.delete_global_resolver_output.DeleteGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_global_resolver

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_global_resolver.delete_global_resolver(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.delete_global_resolver_input.DeleteGlobalResolverInput = {}  # type: ignore[typeddict-item]
        input_["global_resolver_id"] = global_resolver_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_global_resolvers_output.ListGlobalResolversOutput":
        """<p>Lists all Route 53 Global Resolver instances in your account with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of Route 53 Global Resolver instances to return in the response. Valid range is 1-100.</p>
            next_token: <p>The token for the next page of results. This value is returned in the response if there are more results to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_global_resolvers_input.ListGlobalResolversInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_global_resolvers_output.ListGlobalResolversOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_global_resolvers

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_global_resolvers.list_global_resolvers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_global_resolvers_input.ListGlobalResolversInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGlobalResolver:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        regions: "aws_sdk_route53globalresolver.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
        ] = None,
        observability_region: Optional[
            "aws_sdk_route53globalresolver.types.region.Region"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_global_resolver_output.CreateGlobalResolverOutput":
        """<p>Creates a new Route 53 Global Resolver instance. A Route 53 Global Resolver is a global, internet-accessible DNS resolver that provides secure DNS resolution for both public and private domains through global anycast IP addresses.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique string that identifies the request and ensures idempotency. If you make multiple requests with the same client token, only one Route 53 Global Resolver is created.</p>
            description: <p>An optional description for the Route 53 Global Resolver instance. Maximum length of 1024 characters.</p>
            ip_address_type: <p>The IP address type for the Route 53 Global Resolver. Valid values are IPV4 (default) or DUAL_STACK for both IPv4 and IPv6 support.</p>
            name: <p>A descriptive name for the Route 53 Global Resolver instance. Maximum length of 64 characters.</p>
            observability_region: <p>The Amazon Web Services Region where query resolution logs and metrics will be aggregated and delivered. If not specified, logging is not enabled.</p>
            regions: <p>List of Amazon Web Services Regions where the Route 53 Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>
            tags: <p>Tags to associate with the Route 53 Global Resolver. Tags are key-value pairs that help you organize and identify your resources.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.create_global_resolver_input.CreateGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.create_global_resolver_output.CreateGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_global_resolver

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_global_resolver.async_create_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.create_global_resolver_input.CreateGlobalResolverInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        input_["name"] = name
        if observability_region is not None:
            input_["observability_region"] = observability_region
        input_["regions"] = regions
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_global_resolver_output.GetGlobalResolverOutput":
        """<p>Retrieves information about a Route 53 Global Resolver instance.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_global_resolver_input.GetGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_global_resolver_output.GetGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_global_resolver

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_global_resolver.async_get_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_global_resolver_input.GetGlobalResolverInput = {}  # type: ignore[typeddict-item]
        input_["global_resolver_id"] = global_resolver_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        observability_region: Optional[
            "aws_sdk_route53globalresolver.types.region.Region"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
        ] = None,
        regions: Optional["aws_sdk_route53globalresolver.types.regions.Regions"] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_global_resolver_output.UpdateGlobalResolverOutput":
        """<p>Updates the configuration of a Route 53 Global Resolver instance. You can modify the name, description, and observability Region.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Global Resolver.</p>
            name: <p>The name of the Global Resolver.</p>
            observability_region: <p>The Amazon Web Services Regions in which the users' Global Resolver query resolution logs will be propagated.</p>
            description: <p>The description of the Global Resolver.</p>
            ip_address_type: <p>The IP address type for the Global Resolver. Valid values are IPV4 or DUAL_STACK for both IPv4 and IPv6 support.</p>
            regions: <p>The list of Amazon Web Services Regions where the Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.update_global_resolver_input.UpdateGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.update_global_resolver_output.UpdateGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_global_resolver

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_global_resolver.async_update_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.update_global_resolver_input.UpdateGlobalResolverInput = {}  # type: ignore[typeddict-item]
        input_["global_resolver_id"] = global_resolver_id
        if name is not None:
            input_["name"] = name
        if observability_region is not None:
            input_["observability_region"] = observability_region
        if description is not None:
            input_["description"] = description
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_global_resolver_output.DeleteGlobalResolverOutput":
        """<p>Deletes a Route 53 Global Resolver instance. This operation cannot be undone. All associated DNS views, access sources, tokens, and firewall rules are also deleted.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The unique identifier of the Route 53 Global Resolver to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.delete_global_resolver_input.DeleteGlobalResolverInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.delete_global_resolver_output.DeleteGlobalResolverOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_global_resolver

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_global_resolver.async_delete_global_resolver(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.delete_global_resolver_input.DeleteGlobalResolverInput = {}  # type: ignore[typeddict-item]
        input_["global_resolver_id"] = global_resolver_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_global_resolvers_output.ListGlobalResolversOutput":
        """<p>Lists all Route 53 Global Resolver instances in your account with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of Route 53 Global Resolver instances to return in the response. Valid range is 1-100.</p>
            next_token: <p>The token for the next page of results. This value is returned in the response if there are more results to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_global_resolvers_input.ListGlobalResolversInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_global_resolvers_output.ListGlobalResolversOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_global_resolvers

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_global_resolvers.async_list_global_resolvers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_global_resolvers_input.ListGlobalResolversInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
