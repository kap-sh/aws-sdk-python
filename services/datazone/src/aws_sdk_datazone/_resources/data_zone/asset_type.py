from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_type_identifier
    import aws_sdk_datazone.types.create_asset_type_input
    import aws_sdk_datazone.types.create_asset_type_output
    import aws_sdk_datazone.types.delete_asset_type_input
    import aws_sdk_datazone.types.delete_asset_type_output
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.forms_input_map
    import aws_sdk_datazone.types.get_asset_type_input
    import aws_sdk_datazone.types.get_asset_type_output
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.type_name
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class AssetType:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.type_name.TypeName",
        forms_input: "aws_sdk_datazone.types.forms_input_map.FormsInputMap",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
    ) -> "aws_sdk_datazone.types.create_asset_type_output.CreateAssetTypeOutput":
        """<p>Creates a custom asset type.</p> <p>Prerequisites:</p> <ul> <li> <p>The <code>formsInput</code> field is required, however, can be passed as empty (e.g. <code>-forms-input {})</code>. </p> </li> <li> <p>You must have <code>CreateAssetType</code> permissions.</p> </li> <li> <p>The domain-identifier and owning-project-identifier must be valid and active.</p> </li> <li> <p>The name of the asset type must be unique within the domain — duplicate names will cause failure.</p> </li> <li> <p>JSON input must be valid — incorrect formatting causes Invalid JSON errors.</p> </li> </ul>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the custom asset type is being created.</p>
            name: <p>The name of the custom asset type.</p>
            description: <p>The descripton of the custom asset type.</p>
            forms_input: <p>The metadata forms that are to be attached to the custom asset type.</p>
            owning_project_identifier: <p>The identifier of the Amazon DataZone project that is to own the custom asset type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_asset_type_input.CreateAssetTypeInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_asset_type_output.CreateAssetTypeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset_type

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_asset_type.create_asset_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_asset_type_input.CreateAssetTypeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["forms_input"] = forms_input
        input_["owning_project_identifier"] = owning_project_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_asset_type(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput":
        """<p>Deletes an asset type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type must exist in the domain. </p> </li> <li> <p>You must have DeleteAssetType permission.</p> </li> <li> <p>The asset type must not be in use (e.g., assigned to any asset). If used, deletion will fail.</p> </li> <li> <p>You should retrieve the asset type using get-asset-type to confirm its presence before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type is deleted.</p>
            identifier: <p>The identifier of the asset type that is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_asset_type_input.DeleteAssetTypeInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_asset_type

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_asset_type.delete_asset_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_asset_type_input.DeleteAssetTypeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_asset_type(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_asset_type_output.GetAssetTypeOutput":
        """<p>Gets an Amazon DataZone asset type.</p> <p>Asset types define the categories and characteristics of different kinds of data assets within Amazon DataZone.. They determine what metadata fields are required, what operations are possible, and how the asset integrates with other Amazon Web Services services. Asset types can range from built-in types like Amazon S3 buckets and Amazon Web Services Glue tables to custom types defined for specific organizational needs. Understanding asset types is crucial for properly organizing and managing different kinds of data resources.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type with identifier must exist in the domain. ResourceNotFoundException.</p> </li> <li> <p>You must have the GetAssetType permission.</p> </li> <li> <p>Ensure the domain-identifier value is correct and accessible.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type exists.</p>
            identifier: <p>The ID of the asset type.</p>
            revision: <p>The revision of the asset type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_asset_type_input.GetAssetTypeInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_asset_type_output.GetAssetTypeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_asset_type

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_asset_type.get_asset_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_asset_type_input.GetAssetTypeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAssetType:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.type_name.TypeName",
        forms_input: "aws_sdk_datazone.types.forms_input_map.FormsInputMap",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["aws_sdk_datazone.types.description.Description"] = None,
    ) -> "aws_sdk_datazone.types.create_asset_type_output.CreateAssetTypeOutput":
        """<p>Creates a custom asset type.</p> <p>Prerequisites:</p> <ul> <li> <p>The <code>formsInput</code> field is required, however, can be passed as empty (e.g. <code>-forms-input {})</code>. </p> </li> <li> <p>You must have <code>CreateAssetType</code> permissions.</p> </li> <li> <p>The domain-identifier and owning-project-identifier must be valid and active.</p> </li> <li> <p>The name of the asset type must be unique within the domain — duplicate names will cause failure.</p> </li> <li> <p>JSON input must be valid — incorrect formatting causes Invalid JSON errors.</p> </li> </ul>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the custom asset type is being created.</p>
            name: <p>The name of the custom asset type.</p>
            description: <p>The descripton of the custom asset type.</p>
            forms_input: <p>The metadata forms that are to be attached to the custom asset type.</p>
            owning_project_identifier: <p>The identifier of the Amazon DataZone project that is to own the custom asset type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_asset_type_input.CreateAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_asset_type_output.CreateAssetTypeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_asset_type

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_asset_type.async_create_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_asset_type_input.CreateAssetTypeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["forms_input"] = forms_input
        input_["owning_project_identifier"] = owning_project_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset_type(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput":
        """<p>Deletes an asset type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type must exist in the domain. </p> </li> <li> <p>You must have DeleteAssetType permission.</p> </li> <li> <p>The asset type must not be in use (e.g., assigned to any asset). If used, deletion will fail.</p> </li> <li> <p>You should retrieve the asset type using get-asset-type to confirm its presence before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type is deleted.</p>
            identifier: <p>The identifier of the asset type that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_asset_type_input.DeleteAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_asset_type

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_asset_type.async_delete_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_asset_type_input.DeleteAssetTypeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_asset_type(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_asset_type_output.GetAssetTypeOutput":
        """<p>Gets an Amazon DataZone asset type.</p> <p>Asset types define the categories and characteristics of different kinds of data assets within Amazon DataZone.. They determine what metadata fields are required, what operations are possible, and how the asset integrates with other Amazon Web Services services. Asset types can range from built-in types like Amazon S3 buckets and Amazon Web Services Glue tables to custom types defined for specific organizational needs. Understanding asset types is crucial for properly organizing and managing different kinds of data resources.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type with identifier must exist in the domain. ResourceNotFoundException.</p> </li> <li> <p>You must have the GetAssetType permission.</p> </li> <li> <p>Ensure the domain-identifier value is correct and accessible.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type exists.</p>
            identifier: <p>The ID of the asset type.</p>
            revision: <p>The revision of the asset type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_asset_type_input.GetAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_asset_type_output.GetAssetTypeOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_asset_type

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_asset_type.async_get_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_asset_type_input.GetAssetTypeInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
