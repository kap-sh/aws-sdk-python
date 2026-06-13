from typing import Optional, TYPE_CHECKING
from aws_sdk_datazone._services.async_data_zone import ensure_async_iterator
from aws_sdk_datazone._services.data_zone import ensure_sync_iterator
from aws_sdk_datazone._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.asset_name
    import aws_sdk_datazone.types.asset_type_identifier
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.create_asset_input
    import aws_sdk_datazone.types.create_asset_output
    import aws_sdk_datazone.types.create_asset_revision_input
    import aws_sdk_datazone.types.create_asset_revision_output
    import aws_sdk_datazone.types.delete_asset_input
    import aws_sdk_datazone.types.delete_asset_output
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.external_identifier
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.get_asset_input
    import aws_sdk_datazone.types.get_asset_output
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.prediction_configuration
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class Asset:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_datazone.types.asset_name.AssetName",
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        type_identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        external_identifier: Optional[
            "aws_sdk_datazone.types.external_identifier.ExternalIdentifier"
        ] = None,
        type_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        prediction_configuration: Optional[
            "aws_sdk_datazone.types.prediction_configuration.PredictionConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_asset_output.CreateAssetOutput":
        """<p>Creates an asset in Amazon DataZone catalog.</p> <p>Before creating assets, make sure that the following requirements are met:</p> <ul> <li> <p> <code>--domain-identifier</code> must refer to an existing domain.</p> </li> <li> <p> <code>--owning-project-identifier</code> must be a valid project within the domain.</p> </li> <li> <p>Asset type must be created beforehand using <code>create-asset-type</code>, or be a supported system-defined type. For more information, see <a href=\"https://docs.aws.amazon.com/cli/latest/reference/datazone/create-asset-type.html\">create-asset-type</a>.</p> </li> <li> <p> <code>--type-revision</code> (if used) must match a valid revision of the asset type.</p> </li> <li> <p> <code>formsInput</code> is required when it is associated as required in the <code>asset-type</code>. For more information, see <a href=\"https://docs.aws.amazon.com/cli/latest/reference/datazone/create-form-type.html\">create-form-type</a>.</p> </li> <li> <p>Form content must include all required fields as per the form schema (e.g., <code>bucketArn</code>).</p> </li> </ul> <p>You must invoke the following pre-requisite commands before invoking this API:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html\">CreateFormType</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetType.html\">CreateAssetType</a> </p> </li> </ul>

        Args:
            name: <p>Asset name.</p>
            domain_identifier: <p>Amazon DataZone domain where the asset is created.</p>
            external_identifier: <p>The external identifier of the asset.</p> <p>If the value for the <code>externalIdentifier</code> parameter is specified, it must be a unique value.</p>
            type_identifier: <p>The unique identifier of this asset's type.</p>
            type_revision: <p>The revision of this asset's type.</p>
            description: <p>Asset description.</p>
            glossary_terms: <p>Glossary terms attached to the asset.</p>
            forms_input: <p>Metadata forms attached to the asset.</p>
            owning_project_identifier: <p>The unique identifier of the project that owns this asset.</p>
            prediction_configuration: <p>The configuration of the automatically generated business-friendly metadata for the asset.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_asset_input.CreateAssetInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_asset_output.CreateAssetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_asset.create_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.create_asset_input.CreateAssetInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["domain_identifier"] = domain_identifier
        if external_identifier is not None:
            input["external_identifier"] = external_identifier
        input["type_identifier"] = type_identifier
        if type_revision is not None:
            input["type_revision"] = type_revision
        if description is not None:
            input["description"] = description
        if glossary_terms is not None:
            input["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input["forms_input"] = forms_input
        input["owning_project_identifier"] = owning_project_identifier
        if prediction_configuration is not None:
            input["prediction_configuration"] = prediction_configuration
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_asset_output.GetAssetOutput":
        """<p>Gets an Amazon DataZone asset.</p> <p>An asset is the fundamental building block in Amazon DataZone, representing any data resource that needs to be cataloged and managed. It can take many forms, from Amazon S3 buckets and database tables to dashboards and machine learning models. Each asset contains comprehensive metadata about the resource, including its location, schema, ownership, and lineage information. Assets are essential for organizing and managing data resources across an organization, making them discoverable and usable while maintaining proper governance.</p> <p>Before using the Amazon DataZone GetAsset command, ensure the following prerequisites are met:</p> <ul> <li> <p>Domain identifier must exist and be valid</p> </li> <li> <p>Asset identifier must exist</p> </li> <li> <p>User must have the required permissions to perform the action</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain to which the asset belongs.</p>
            identifier: <p>The ID of the Amazon DataZone asset.</p> <p>This parameter supports either the value of <code>assetId</code> or <code>externalIdentifier</code> as input. If you are passing the value of <code>externalIdentifier</code>, you must prefix this value with <code>externalIdentifer%2F</code>.</p>
            revision: <p>The revision of the Amazon DataZone asset.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_asset_input.GetAssetInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_asset_output.GetAssetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_asset

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_asset.get_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.get_asset_input.GetAssetInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier
        if revision is not None:
            input["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_asset_output.DeleteAssetOutput":
        """<p>Deletes an asset in Amazon DataZone.</p> <ul> <li> <p>--domain-identifier must refer to a valid and existing domain. </p> </li> <li> <p>--identifier must refer to an existing asset in the specified domain.</p> </li> <li> <p>Asset must not be referenced in any existing asset filters.</p> </li> <li> <p>Asset must not be linked to any draft or published data product.</p> </li> <li> <p>User must have delete permissions for the domain and project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset is deleted.</p>
            identifier: <p>The identifier of the asset that is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_asset_input.DeleteAssetInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_asset_output.DeleteAssetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_asset

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_asset.delete_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.delete_asset_input.DeleteAssetInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_asset_revision(
        self,
        name: "aws_sdk_datazone.types.asset_name.AssetName",
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        type_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        prediction_configuration: Optional[
            "aws_sdk_datazone.types.prediction_configuration.PredictionConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_datazone.types.create_asset_revision_output.CreateAssetRevisionOutput"
    ):
        """<p>Creates a revision of the asset.</p> <p>Asset revisions represent new versions of existing assets, capturing changes to either the underlying data or its metadata. They maintain a historical record of how assets evolve over time, who made changes, and when those changes occurred. This versioning capability is crucial for governance and compliance, allowing organizations to track changes, understand their impact, and roll back if necessary.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must already exist in the domain with identifier. </p> </li> <li> <p> <code>formsInput</code> is required when asset has the form type. <code>typeRevision</code> should be the latest version of form type. </p> </li> <li> <p>The form content must include all required fields (e.g., <code>bucketArn</code> for <code>S3ObjectCollectionForm</code>).</p> </li> <li> <p>The owning project of the original asset must still exist and be active.</p> </li> <li> <p>User must have write access to the project and domain.</p> </li> </ul>

        Args:
            name: <p>Te revised name of the asset.</p>
            domain_identifier: <p>The unique identifier of the domain where the asset is being revised.</p>
            identifier: <p>The identifier of the asset.</p>
            type_revision: <p>The revision type of the asset.</p>
            description: <p>The revised description of the asset.</p>
            glossary_terms: <p>The glossary terms to be attached to the asset as part of asset revision.</p>
            forms_input: <p>The metadata forms to be attached to the asset as part of asset revision.</p>
            prediction_configuration: <p>The configuration of the automatically generated business-friendly metadata for the asset.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_asset_revision_input.CreateAssetRevisionInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_asset_revision_output.CreateAssetRevisionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset_revision

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_asset_revision.create_asset_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.create_asset_revision_input.CreateAssetRevisionInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier
        if type_revision is not None:
            input["type_revision"] = type_revision
        if description is not None:
            input["description"] = description
        if glossary_terms is not None:
            input["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input["forms_input"] = forms_input
        if prediction_configuration is not None:
            input["prediction_configuration"] = prediction_configuration
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAsset:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_datazone.types.asset_name.AssetName",
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        type_identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        external_identifier: Optional[
            "aws_sdk_datazone.types.external_identifier.ExternalIdentifier"
        ] = None,
        type_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        prediction_configuration: Optional[
            "aws_sdk_datazone.types.prediction_configuration.PredictionConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_asset_output.CreateAssetOutput":
        """<p>Creates an asset in Amazon DataZone catalog.</p> <p>Before creating assets, make sure that the following requirements are met:</p> <ul> <li> <p> <code>--domain-identifier</code> must refer to an existing domain.</p> </li> <li> <p> <code>--owning-project-identifier</code> must be a valid project within the domain.</p> </li> <li> <p>Asset type must be created beforehand using <code>create-asset-type</code>, or be a supported system-defined type. For more information, see <a href=\"https://docs.aws.amazon.com/cli/latest/reference/datazone/create-asset-type.html\">create-asset-type</a>.</p> </li> <li> <p> <code>--type-revision</code> (if used) must match a valid revision of the asset type.</p> </li> <li> <p> <code>formsInput</code> is required when it is associated as required in the <code>asset-type</code>. For more information, see <a href=\"https://docs.aws.amazon.com/cli/latest/reference/datazone/create-form-type.html\">create-form-type</a>.</p> </li> <li> <p>Form content must include all required fields as per the form schema (e.g., <code>bucketArn</code>).</p> </li> </ul> <p>You must invoke the following pre-requisite commands before invoking this API:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html\">CreateFormType</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetType.html\">CreateAssetType</a> </p> </li> </ul>

        Args:
            name: <p>Asset name.</p>
            domain_identifier: <p>Amazon DataZone domain where the asset is created.</p>
            external_identifier: <p>The external identifier of the asset.</p> <p>If the value for the <code>externalIdentifier</code> parameter is specified, it must be a unique value.</p>
            type_identifier: <p>The unique identifier of this asset's type.</p>
            type_revision: <p>The revision of this asset's type.</p>
            description: <p>Asset description.</p>
            glossary_terms: <p>Glossary terms attached to the asset.</p>
            forms_input: <p>Metadata forms attached to the asset.</p>
            owning_project_identifier: <p>The unique identifier of the project that owns this asset.</p>
            prediction_configuration: <p>The configuration of the automatically generated business-friendly metadata for the asset.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_asset_input.CreateAssetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_asset_output.CreateAssetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.create_asset_input.CreateAssetInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["domain_identifier"] = domain_identifier
        if external_identifier is not None:
            input["external_identifier"] = external_identifier
        input["type_identifier"] = type_identifier
        if type_revision is not None:
            input["type_revision"] = type_revision
        if description is not None:
            input["description"] = description
        if glossary_terms is not None:
            input["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input["forms_input"] = forms_input
        input["owning_project_identifier"] = owning_project_identifier
        if prediction_configuration is not None:
            input["prediction_configuration"] = prediction_configuration
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_asset_output.GetAssetOutput":
        """<p>Gets an Amazon DataZone asset.</p> <p>An asset is the fundamental building block in Amazon DataZone, representing any data resource that needs to be cataloged and managed. It can take many forms, from Amazon S3 buckets and database tables to dashboards and machine learning models. Each asset contains comprehensive metadata about the resource, including its location, schema, ownership, and lineage information. Assets are essential for organizing and managing data resources across an organization, making them discoverable and usable while maintaining proper governance.</p> <p>Before using the Amazon DataZone GetAsset command, ensure the following prerequisites are met:</p> <ul> <li> <p>Domain identifier must exist and be valid</p> </li> <li> <p>Asset identifier must exist</p> </li> <li> <p>User must have the required permissions to perform the action</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain to which the asset belongs.</p>
            identifier: <p>The ID of the Amazon DataZone asset.</p> <p>This parameter supports either the value of <code>assetId</code> or <code>externalIdentifier</code> as input. If you are passing the value of <code>externalIdentifier</code>, you must prefix this value with <code>externalIdentifer%2F</code>.</p>
            revision: <p>The revision of the Amazon DataZone asset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_asset_input.GetAssetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_asset_output.GetAssetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_asset

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_asset.async_get_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.get_asset_input.GetAssetInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier
        if revision is not None:
            input["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_asset_output.DeleteAssetOutput":
        """<p>Deletes an asset in Amazon DataZone.</p> <ul> <li> <p>--domain-identifier must refer to a valid and existing domain. </p> </li> <li> <p>--identifier must refer to an existing asset in the specified domain.</p> </li> <li> <p>Asset must not be referenced in any existing asset filters.</p> </li> <li> <p>Asset must not be linked to any draft or published data product.</p> </li> <li> <p>User must have delete permissions for the domain and project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset is deleted.</p>
            identifier: <p>The identifier of the asset that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_asset_input.DeleteAssetInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_asset_output.DeleteAssetOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_asset

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.delete_asset_input.DeleteAssetInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_asset_revision(
        self,
        name: "aws_sdk_datazone.types.asset_name.AssetName",
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        prediction_configuration: Optional[
            "aws_sdk_datazone.types.prediction_configuration.PredictionConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_datazone.types.create_asset_revision_output.CreateAssetRevisionOutput"
    ):
        """<p>Creates a revision of the asset.</p> <p>Asset revisions represent new versions of existing assets, capturing changes to either the underlying data or its metadata. They maintain a historical record of how assets evolve over time, who made changes, and when those changes occurred. This versioning capability is crucial for governance and compliance, allowing organizations to track changes, understand their impact, and roll back if necessary.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must already exist in the domain with identifier. </p> </li> <li> <p> <code>formsInput</code> is required when asset has the form type. <code>typeRevision</code> should be the latest version of form type. </p> </li> <li> <p>The form content must include all required fields (e.g., <code>bucketArn</code> for <code>S3ObjectCollectionForm</code>).</p> </li> <li> <p>The owning project of the original asset must still exist and be active.</p> </li> <li> <p>User must have write access to the project and domain.</p> </li> </ul>

        Args:
            name: <p>Te revised name of the asset.</p>
            domain_identifier: <p>The unique identifier of the domain where the asset is being revised.</p>
            identifier: <p>The identifier of the asset.</p>
            type_revision: <p>The revision type of the asset.</p>
            description: <p>The revised description of the asset.</p>
            glossary_terms: <p>The glossary terms to be attached to the asset as part of asset revision.</p>
            forms_input: <p>The metadata forms to be attached to the asset as part of asset revision.</p>
            prediction_configuration: <p>The configuration of the automatically generated business-friendly metadata for the asset.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_asset_revision_input.CreateAssetRevisionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_asset_revision_output.CreateAssetRevisionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset_revision

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_asset_revision.async_create_asset_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.create_asset_revision_input.CreateAssetRevisionInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier
        if type_revision is not None:
            input["type_revision"] = type_revision
        if description is not None:
            input["description"] = description
        if glossary_terms is not None:
            input["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input["forms_input"] = forms_input
        if prediction_configuration is not None:
            input["prediction_configuration"] = prediction_configuration
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
