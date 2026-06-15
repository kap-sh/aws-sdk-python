from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_selling._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.create_resource_snapshot_request
    import aws_sdk_partnercentral_selling.types.create_resource_snapshot_response
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.engagement_resource_association_summary
    import aws_sdk_partnercentral_selling.types.get_resource_snapshot_request
    import aws_sdk_partnercentral_selling.types.get_resource_snapshot_response
    import aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_request
    import aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_response
    import aws_sdk_partnercentral_selling.types.list_resource_snapshots_request
    import aws_sdk_partnercentral_selling.types.list_resource_snapshots_response
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_revision
    import aws_sdk_partnercentral_selling.types.resource_snapshot_summary
    import aws_sdk_partnercentral_selling.types.resource_template_name
    import aws_sdk_partnercentral_selling.types.resource_type
    from aws_sdk_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from aws_sdk_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class ResourceSnapshot:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create_resource_snapshot(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_resource_snapshot_response.CreateResourceSnapshotResponse":
        """<p> This action allows you to create an immutable snapshot of a specific resource, such as an opportunity, within the context of an engagement. The snapshot captures a subset of the resource's data based on the schema defined by the provided template.</p>

        Args:
            catalog: <p> Specifies the catalog where the snapshot is created. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            engagement_identifier: <p> The unique identifier of the engagement associated with this snapshot. This field links the snapshot to a specific engagement context. </p>
            resource_type: <p> Specifies the type of resource for which the snapshot is being created. This field determines the structure and content of the snapshot. Must be one of the supported resource types, such as: <code>Opportunity</code>. </p>
            resource_identifier: <p> The unique identifier of the specific resource to be snapshotted. The format and constraints of this identifier depend on the <code>ResourceType</code> specified. For example: For <code>Opportunity</code> type, it will be an opportunity ID. </p>
            resource_snapshot_template_identifier: <p> The name of the template that defines the schema for the snapshot. This template determines which subset of the resource data will be included in the snapshot. Must correspond to an existing and valid template for the specified <code>ResourceType</code>. </p>
            client_token: <p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate snapshot creations. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.create_resource_snapshot_request.CreateResourceSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.create_resource_snapshot_response.CreateResourceSnapshotResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot.create_resource_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.create_resource_snapshot_request.CreateResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["engagement_identifier"] = engagement_identifier
        input_["resource_type"] = resource_type
        input_["resource_identifier"] = resource_identifier
        input_["resource_snapshot_template_identifier"] = (
            resource_snapshot_template_identifier
        )
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_snapshot(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        revision: Optional[
            "aws_sdk_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_resource_snapshot_response.GetResourceSnapshotResponse":
        """<p>Use this action to retrieve a specific snapshot record.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Retrieves the snapshot from the production AWS environment.</p> </li> <li> <p>Sandbox: Retrieves the snapshot from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            engagement_identifier: <p>The unique identifier of the engagement associated with the snapshot. This field links the snapshot to a specific engagement context.</p>
            resource_type: <p>Specifies the type of resource that was snapshotted. This field determines the structure and content of the snapshot payload. Valid value includes:<code>Opportunity</code>: For opportunity-related data. </p>
            resource_identifier: <p>The unique identifier of the specific resource that was snapshotted. The format and constraints of this identifier depend on the ResourceType specified. For <code>Opportunity</code> type, it will be an <code>opportunity ID</code> </p>
            resource_snapshot_template_identifier: <p>he name of the template that defines the schema for the snapshot. This template determines which subset of the resource data is included in the snapshot and must correspond to an existing and valid template for the specified <code>ResourceType</code>.</p>
            revision: <p>Specifies which revision of the snapshot to retrieve. If omitted returns the latest revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.get_resource_snapshot_request.GetResourceSnapshotRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.get_resource_snapshot_response.GetResourceSnapshotResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot.get_resource_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.get_resource_snapshot_request.GetResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["engagement_identifier"] = engagement_identifier
        input_["resource_type"] = resource_type
        input_["resource_identifier"] = resource_identifier
        input_["resource_snapshot_template_identifier"] = (
            resource_snapshot_template_identifier
        )
        if revision is not None:
            input_["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_engagement_resource_associations(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        resource_type: Optional[
            "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_response.ListEngagementResourceAssociationsResponse":
        r"""<p>Lists the associations between resources and engagements where the caller is a member and has at least one snapshot in the engagement.</p>

        Args:
            catalog: <p>Specifies the catalog in which to search for engagement-resource associations. Valid Values: \"AWS\" or \"Sandbox\"</p> <ul> <li> <p> <code>AWS</code> for production environments.</p> </li> <li> <p> <code>Sandbox</code> for testing and development purposes.</p> </li> </ul>
            max_results: <p>Limits the number of results returned in a single call. Use this to control the number of results returned, especially useful for pagination.</p>
            next_token: <p>A token used for pagination of results. Include this token in subsequent requests to retrieve the next set of results.</p>
            engagement_identifier: <p>Filters the results to include only associations related to the specified engagement. Use this when you want to find all resources associated with a specific engagement.</p>
            resource_type: <p> Filters the results to include only associations with resources of the specified type. </p>
            resource_identifier: <p>Filters the results to include only associations with the specified resource. Varies depending on the resource type. Use this when you want to find all engagements associated with a specific resource.</p>
            created_by: <p>Filters the response to include only snapshots of resources owned by the specified AWS account ID. Use this when you want to find associations related to resources owned by a particular account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_request.ListEngagementResourceAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_response.ListEngagementResourceAssociationsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_resource_associations

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_resource_associations.list_engagement_resource_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_request.ListEngagementResourceAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if created_by is not None:
            input_["created_by"] = created_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_resource_snapshots(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        resource_type: Optional[
            "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        resource_snapshot_template_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
        ] = None,
        created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_resource_snapshots_response.ListResourceSnapshotsResponse":
        """<p>Retrieves a list of resource view snapshots based on specified criteria. This operation supports various use cases, including: </p> <ul> <li> <p>Fetching all snapshots associated with an engagement.</p> </li> <li> <p>Retrieving snapshots of a specific resource type within an engagement.</p> </li> <li> <p>Obtaining snapshots for a particular resource using a specified template.</p> </li> <li> <p>Accessing the latest snapshot of a resource within an engagement.</p> </li> <li> <p>Filtering snapshots by resource owner.</p> </li> </ul>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The unique identifier of the engagement associated with the snapshots. </p>
            resource_type: <p> Filters the response to include only snapshots of the specified resource type. </p>
            resource_identifier: <p> Filters the response to include only snapshots of the specified resource. </p>
            resource_snapshot_template_identifier: <p>Filters the response to include only snapshots created using the specified template.</p>
            created_by: <p>Filters the response to include only snapshots of resources owned by the specified AWS account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_resource_snapshots_request.ListResourceSnapshotsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_resource_snapshots_response.ListResourceSnapshotsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshots

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshots.list_resource_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_resource_snapshots_request.ListResourceSnapshotsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["engagement_identifier"] = engagement_identifier
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if resource_snapshot_template_identifier is not None:
            input_["resource_snapshot_template_identifier"] = (
                resource_snapshot_template_identifier
            )
        if created_by is not None:
            input_["created_by"] = created_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncResourceSnapshot:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create_resource_snapshot(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_resource_snapshot_response.CreateResourceSnapshotResponse":
        """<p> This action allows you to create an immutable snapshot of a specific resource, such as an opportunity, within the context of an engagement. The snapshot captures a subset of the resource's data based on the schema defined by the provided template.</p>

        Args:
            catalog: <p> Specifies the catalog where the snapshot is created. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            engagement_identifier: <p> The unique identifier of the engagement associated with this snapshot. This field links the snapshot to a specific engagement context. </p>
            resource_type: <p> Specifies the type of resource for which the snapshot is being created. This field determines the structure and content of the snapshot. Must be one of the supported resource types, such as: <code>Opportunity</code>. </p>
            resource_identifier: <p> The unique identifier of the specific resource to be snapshotted. The format and constraints of this identifier depend on the <code>ResourceType</code> specified. For example: For <code>Opportunity</code> type, it will be an opportunity ID. </p>
            resource_snapshot_template_identifier: <p> The name of the template that defines the schema for the snapshot. This template determines which subset of the resource data will be included in the snapshot. Must correspond to an existing and valid template for the specified <code>ResourceType</code>. </p>
            client_token: <p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate snapshot creations. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.create_resource_snapshot_request.CreateResourceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.create_resource_snapshot_response.CreateResourceSnapshotResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot.async_create_resource_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.create_resource_snapshot_request.CreateResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["engagement_identifier"] = engagement_identifier
        input_["resource_type"] = resource_type
        input_["resource_identifier"] = resource_identifier
        input_["resource_snapshot_template_identifier"] = (
            resource_snapshot_template_identifier
        )
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_snapshot(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        revision: Optional[
            "aws_sdk_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_resource_snapshot_response.GetResourceSnapshotResponse":
        """<p>Use this action to retrieve a specific snapshot record.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Retrieves the snapshot from the production AWS environment.</p> </li> <li> <p>Sandbox: Retrieves the snapshot from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            engagement_identifier: <p>The unique identifier of the engagement associated with the snapshot. This field links the snapshot to a specific engagement context.</p>
            resource_type: <p>Specifies the type of resource that was snapshotted. This field determines the structure and content of the snapshot payload. Valid value includes:<code>Opportunity</code>: For opportunity-related data. </p>
            resource_identifier: <p>The unique identifier of the specific resource that was snapshotted. The format and constraints of this identifier depend on the ResourceType specified. For <code>Opportunity</code> type, it will be an <code>opportunity ID</code> </p>
            resource_snapshot_template_identifier: <p>he name of the template that defines the schema for the snapshot. This template determines which subset of the resource data is included in the snapshot and must correspond to an existing and valid template for the specified <code>ResourceType</code>.</p>
            revision: <p>Specifies which revision of the snapshot to retrieve. If omitted returns the latest revision.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.get_resource_snapshot_request.GetResourceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.get_resource_snapshot_response.GetResourceSnapshotResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot.async_get_resource_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.get_resource_snapshot_request.GetResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["engagement_identifier"] = engagement_identifier
        input_["resource_type"] = resource_type
        input_["resource_identifier"] = resource_identifier
        input_["resource_snapshot_template_identifier"] = (
            resource_snapshot_template_identifier
        )
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_engagement_resource_associations(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        resource_type: Optional[
            "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_response.ListEngagementResourceAssociationsResponse":
        r"""<p>Lists the associations between resources and engagements where the caller is a member and has at least one snapshot in the engagement.</p>

        Args:
            catalog: <p>Specifies the catalog in which to search for engagement-resource associations. Valid Values: \"AWS\" or \"Sandbox\"</p> <ul> <li> <p> <code>AWS</code> for production environments.</p> </li> <li> <p> <code>Sandbox</code> for testing and development purposes.</p> </li> </ul>
            max_results: <p>Limits the number of results returned in a single call. Use this to control the number of results returned, especially useful for pagination.</p>
            next_token: <p>A token used for pagination of results. Include this token in subsequent requests to retrieve the next set of results.</p>
            engagement_identifier: <p>Filters the results to include only associations related to the specified engagement. Use this when you want to find all resources associated with a specific engagement.</p>
            resource_type: <p> Filters the results to include only associations with resources of the specified type. </p>
            resource_identifier: <p>Filters the results to include only associations with the specified resource. Varies depending on the resource type. Use this when you want to find all engagements associated with a specific resource.</p>
            created_by: <p>Filters the response to include only snapshots of resources owned by the specified AWS account ID. Use this when you want to find associations related to resources owned by a particular account. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_request.ListEngagementResourceAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_response.ListEngagementResourceAssociationsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_resource_associations

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_resource_associations.async_list_engagement_resource_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_engagement_resource_associations_request.ListEngagementResourceAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if created_by is not None:
            input_["created_by"] = created_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_resource_snapshots(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        resource_type: Optional[
            "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
        ] = None,
        resource_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
        ] = None,
        resource_snapshot_template_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
        ] = None,
        created_by: Optional[
            "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_resource_snapshots_response.ListResourceSnapshotsResponse":
        """<p>Retrieves a list of resource view snapshots based on specified criteria. This operation supports various use cases, including: </p> <ul> <li> <p>Fetching all snapshots associated with an engagement.</p> </li> <li> <p>Retrieving snapshots of a specific resource type within an engagement.</p> </li> <li> <p>Obtaining snapshots for a particular resource using a specified template.</p> </li> <li> <p>Accessing the latest snapshot of a resource within an engagement.</p> </li> <li> <p>Filtering snapshots by resource owner.</p> </li> </ul>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The unique identifier of the engagement associated with the snapshots. </p>
            resource_type: <p> Filters the response to include only snapshots of the specified resource type. </p>
            resource_identifier: <p> Filters the response to include only snapshots of the specified resource. </p>
            resource_snapshot_template_identifier: <p>Filters the response to include only snapshots created using the specified template.</p>
            created_by: <p>Filters the response to include only snapshots of resources owned by the specified AWS account. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_resource_snapshots_request.ListResourceSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_resource_snapshots_response.ListResourceSnapshotsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshots

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshots.async_list_resource_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_selling.types.list_resource_snapshots_request.ListResourceSnapshotsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["engagement_identifier"] = engagement_identifier
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if resource_snapshot_template_identifier is not None:
            input_["resource_snapshot_template_identifier"] = (
                resource_snapshot_template_identifier
            )
        if created_by is not None:
            input_["created_by"] = created_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
