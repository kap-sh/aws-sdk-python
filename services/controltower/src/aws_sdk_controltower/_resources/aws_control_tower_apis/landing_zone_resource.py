from typing import TYPE_CHECKING, Optional

import aws_sdk_controltower._auth._signers
import aws_sdk_controltower._auth._sigv4
from aws_sdk_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_controltower.types.create_landing_zone_input
    import aws_sdk_controltower.types.create_landing_zone_output
    import aws_sdk_controltower.types.delete_landing_zone_input
    import aws_sdk_controltower.types.delete_landing_zone_output
    import aws_sdk_controltower.types.get_landing_zone_input
    import aws_sdk_controltower.types.get_landing_zone_output
    import aws_sdk_controltower.types.landing_zone_summary
    import aws_sdk_controltower.types.landing_zone_version
    import aws_sdk_controltower.types.list_landing_zones_input
    import aws_sdk_controltower.types.list_landing_zones_max_results
    import aws_sdk_controltower.types.list_landing_zones_output
    import aws_sdk_controltower.types.manifest
    import aws_sdk_controltower.types.remediation_types
    import aws_sdk_controltower.types.reset_landing_zone_input
    import aws_sdk_controltower.types.reset_landing_zone_output
    import aws_sdk_controltower.types.tag_map
    import aws_sdk_controltower.types.update_landing_zone_input
    import aws_sdk_controltower.types.update_landing_zone_output
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class LandingZoneResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def create(
        self,
        version: "aws_sdk_controltower.types.landing_zone_version.LandingZoneVersion",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        remediation_types: Optional[
            "aws_sdk_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        tags: Optional["aws_sdk_controltower.types.tag_map.TagMap"] = None,
        manifest: Optional["aws_sdk_controltower.types.manifest.Manifest"] = None,
    ) -> (
        "aws_sdk_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
    ):
        """<p>Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.</p>

        Args:
            version: <p>The landing zone version, for example, 3.0.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.</p>
            tags: <p>Tags to be applied to the landing zone. </p>
            manifest: <p>The manifest JSON file is a text file that describes your Amazon Web Services resources. For examples, review <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch\">Launch your landing zone</a>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.create_landing_zone_input.CreateLandingZoneInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.create_landing_zone

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.create_landing_zone.create_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.create_landing_zone_input.CreateLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["version"] = version
        if remediation_types is not None:
            input["remediation_types"] = remediation_types
        if tags is not None:
            input["tags"] = tags
        if manifest is not None:
            input["manifest"] = manifest

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_landing_zone_output.GetLandingZoneOutput":
        """<p>Returns details about the landing zone. Displays a message in case of error.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.get_landing_zone_input.GetLandingZoneInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.get_landing_zone_output.GetLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone.get_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.get_landing_zone_input.GetLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["landing_zone_identifier"] = landing_zone_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        version: "aws_sdk_controltower.types.landing_zone_version.LandingZoneVersion",
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        remediation_types: Optional[
            "aws_sdk_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        manifest: Optional["aws_sdk_controltower.types.manifest.Manifest"] = None,
    ) -> (
        "aws_sdk_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
    ):
        """<p>This API call updates the landing zone. It starts an asynchronous operation that updates the landing zone based on the new landing zone version, or on the changed parameters specified in the updated manifest file. </p>

        Args:
            version: <p>The landing zone version, for example, 3.2.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when updating the landing zone configuration.</p>
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
            manifest: <p>The manifest file (JSON) is a text file that describes your Amazon Web Services resources. For an example, review <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch\">Launch your landing zone</a>. The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.update_landing_zone_input.UpdateLandingZoneInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.update_landing_zone

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.update_landing_zone.update_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.update_landing_zone_input.UpdateLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["version"] = version
        if remediation_types is not None:
            input["remediation_types"] = remediation_types
        input["landing_zone_identifier"] = landing_zone_identifier
        if manifest is not None:
            input["manifest"] = manifest

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> (
        "aws_sdk_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
    ):
        """<p>Decommissions a landing zone. This API call starts an asynchronous operation that deletes Amazon Web Services Control Tower resources deployed in accounts managed by Amazon Web Services Control Tower.</p> <p>Decommissioning a landing zone is a process with significant consequences, and it cannot be undone. We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.delete_landing_zone

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.delete_landing_zone.delete_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["landing_zone_identifier"] = landing_zone_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_landing_zones_output.ListLandingZonesOutput":
        """<p>Returns the landing zone ARN for the landing zone deployed in your managed account. This API also creates an ARN for existing accounts that do not yet have a landing zone ARN. </p> <p>Returns one landing zone ARN.</p>

        Args:
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>The maximum number of returned landing zone ARNs, which is one.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.list_landing_zones_input.ListLandingZonesInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.list_landing_zones_output.ListLandingZonesOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zones

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zones.list_landing_zones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.list_landing_zones_input.ListLandingZonesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reset_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput":
        """<p>This API call resets a landing zone. It starts an asynchronous operation that resets the landing zone to the parameters specified in the original configuration, which you specified in the manifest file. Nothing in the manifest file's original landing zone configuration is changed during the reset process, by default. This API is not the same as a rollback of a landing zone version, which is not a supported operation.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.reset_landing_zone_input.ResetLandingZoneInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.reset_landing_zone

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.reset_landing_zone.reset_landing_zone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.reset_landing_zone_input.ResetLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["landing_zone_identifier"] = landing_zone_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLandingZoneResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def create(
        self,
        version: "aws_sdk_controltower.types.landing_zone_version.LandingZoneVersion",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        remediation_types: Optional[
            "aws_sdk_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        tags: Optional["aws_sdk_controltower.types.tag_map.TagMap"] = None,
        manifest: Optional["aws_sdk_controltower.types.manifest.Manifest"] = None,
    ) -> (
        "aws_sdk_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
    ):
        """<p>Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.</p>

        Args:
            version: <p>The landing zone version, for example, 3.0.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.</p>
            tags: <p>Tags to be applied to the landing zone. </p>
            manifest: <p>The manifest JSON file is a text file that describes your Amazon Web Services resources. For examples, review <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch\">Launch your landing zone</a>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.create_landing_zone_input.CreateLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.create_landing_zone

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.create_landing_zone.async_create_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.create_landing_zone_input.CreateLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["version"] = version
        if remediation_types is not None:
            input["remediation_types"] = remediation_types
        if tags is not None:
            input["tags"] = tags
        if manifest is not None:
            input["manifest"] = manifest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_landing_zone_output.GetLandingZoneOutput":
        """<p>Returns details about the landing zone. Displays a message in case of error.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.get_landing_zone_input.GetLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.get_landing_zone_output.GetLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone.async_get_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.get_landing_zone_input.GetLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["landing_zone_identifier"] = landing_zone_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        version: "aws_sdk_controltower.types.landing_zone_version.LandingZoneVersion",
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        remediation_types: Optional[
            "aws_sdk_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        manifest: Optional["aws_sdk_controltower.types.manifest.Manifest"] = None,
    ) -> (
        "aws_sdk_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
    ):
        """<p>This API call updates the landing zone. It starts an asynchronous operation that updates the landing zone based on the new landing zone version, or on the changed parameters specified in the updated manifest file. </p>

        Args:
            version: <p>The landing zone version, for example, 3.2.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when updating the landing zone configuration.</p>
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
            manifest: <p>The manifest file (JSON) is a text file that describes your Amazon Web Services resources. For an example, review <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch\">Launch your landing zone</a>. The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.update_landing_zone_input.UpdateLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.update_landing_zone

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.update_landing_zone.async_update_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.update_landing_zone_input.UpdateLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["version"] = version
        if remediation_types is not None:
            input["remediation_types"] = remediation_types
        input["landing_zone_identifier"] = landing_zone_identifier
        if manifest is not None:
            input["manifest"] = manifest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> (
        "aws_sdk_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
    ):
        """<p>Decommissions a landing zone. This API call starts an asynchronous operation that deletes Amazon Web Services Control Tower resources deployed in accounts managed by Amazon Web Services Control Tower.</p> <p>Decommissioning a landing zone is a process with significant consequences, and it cannot be undone. We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.delete_landing_zone

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.delete_landing_zone.async_delete_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["landing_zone_identifier"] = landing_zone_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_landing_zones_output.ListLandingZonesOutput":
        """<p>Returns the landing zone ARN for the landing zone deployed in your managed account. This API also creates an ARN for existing accounts that do not yet have a landing zone ARN. </p> <p>Returns one landing zone ARN.</p>

        Args:
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>The maximum number of returned landing zone ARNs, which is one.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.list_landing_zones_input.ListLandingZonesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.list_landing_zones_output.ListLandingZonesOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zones

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zones.async_list_landing_zones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.list_landing_zones_input.ListLandingZonesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput":
        """<p>This API call resets a landing zone. It starts an asynchronous operation that resets the landing zone to the parameters specified in the original configuration, which you specified in the manifest file. Nothing in the manifest file's original landing zone configuration is changed during the reset process, by default. This API is not the same as a rollback of a landing zone version, which is not a supported operation.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.reset_landing_zone_input.ResetLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.reset_landing_zone

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.reset_landing_zone.async_reset_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_controltower.types.reset_landing_zone_input.ResetLandingZoneInput = {}  # type: ignore[typeddict-item]
        input["landing_zone_identifier"] = landing_zone_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
