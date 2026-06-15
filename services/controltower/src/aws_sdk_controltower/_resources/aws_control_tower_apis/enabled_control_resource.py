from __future__ import annotations

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
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.control_identifier
    import aws_sdk_controltower.types.enable_control_input
    import aws_sdk_controltower.types.enable_control_output
    import aws_sdk_controltower.types.enabled_control_filter
    import aws_sdk_controltower.types.enabled_control_parameters
    import aws_sdk_controltower.types.enabled_control_summary
    import aws_sdk_controltower.types.get_enabled_control_input
    import aws_sdk_controltower.types.get_enabled_control_output
    import aws_sdk_controltower.types.list_enabled_controls_input
    import aws_sdk_controltower.types.list_enabled_controls_output
    import aws_sdk_controltower.types.max_results
    import aws_sdk_controltower.types.reset_enabled_control_input
    import aws_sdk_controltower.types.reset_enabled_control_output
    import aws_sdk_controltower.types.tag_map
    import aws_sdk_controltower.types.target_identifier
    import aws_sdk_controltower.types.update_enabled_control_input
    import aws_sdk_controltower.types.update_enabled_control_output
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class EnabledControlResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def create(
        self,
        control_identifier: "aws_sdk_controltower.types.control_identifier.ControlIdentifier",
        target_identifier: "aws_sdk_controltower.types.target_identifier.TargetIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        tags: Optional["aws_sdk_controltower.types.tag_map.TagMap"] = None,
        parameters: Optional[
            "aws_sdk_controltower.types.enabled_control_parameters.EnabledControlParameters"
        ] = None,
    ) -> "aws_sdk_controltower.types.enable_control_output.EnableControlOutput":
        r"""<p>This API call activates a control. It starts an asynchronous operation that creates Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            tags: <p>Tags to be applied to the <code>EnabledControl</code> resource.</p>
            parameters: <p>A list of input parameter values, which are specified to configure the control when you enable it.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.enable_control_input.EnableControlInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.enable_control_output.EnableControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.enable_control

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.enable_control.enable_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.enable_control_input.EnableControlInput = {}  # type: ignore[typeddict-item]
        input_["control_identifier"] = control_identifier
        input_["target_identifier"] = target_identifier
        if tags is not None:
            input_["tags"] = tags
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> (
        "aws_sdk_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
    ):
        r"""<p>Retrieves details about an enabled control. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            enabled_control_identifier: <p>The <code>controlIdentifier</code> of the enabled control.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.get_enabled_control_input.GetEnabledControlInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_enabled_control

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.get_enabled_control.get_enabled_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_enabled_control_input.GetEnabledControlInput = {}  # type: ignore[typeddict-item]
        input_["enabled_control_identifier"] = enabled_control_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        parameters: "aws_sdk_controltower.types.enabled_control_parameters.EnabledControlParameters",
        enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput":
        r"""<p> Updates the configuration of an already enabled control.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of SUCCEEDED, supply parameters that are different from the currently configured parameters. Otherwise, Amazon Web Services Control Tower will not accept the request.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of FAILED, Amazon Web Services Control Tower updates the control to match any valid parameters that you supply.</p> <p>If the <code>DriftSummary</code> status for the control shows as <code>DRIFTED</code>, you cannot call this API. Instead, you can update the control by calling the <code>ResetEnabledControl</code> API. Alternatively, you can call <code>DisableControl</code> and then call <code>EnableControl</code> again. Also, you can run an extending governance operation to repair drift. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>. </p>

        Args:
            parameters: <p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>
            enabled_control_identifier: <p> The ARN of the enabled control that will be updated. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.update_enabled_control_input.UpdateEnabledControlInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.update_enabled_control

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.update_enabled_control.update_enabled_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.update_enabled_control_input.UpdateEnabledControlInput = {}  # type: ignore[typeddict-item]
        input_["parameters"] = parameters
        input_["enabled_control_identifier"] = enabled_control_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        target_identifier: Optional[
            "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_controltower.types.enabled_control_filter.EnabledControlFilter"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "aws_sdk_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput":
        r"""<p>Lists the controls enabled by Amazon Web Services Control Tower on the specified organizational unit and the accounts it contains. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
            filter: <p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>
            include_children: <p>A boolean value that determines whether to include enabled controls from child organizational units in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.list_enabled_controls_input.ListEnabledControlsInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_enabled_controls

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.list_enabled_controls.list_enabled_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_enabled_controls_input.ListEnabledControlsInput = {}  # type: ignore[typeddict-item]
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if include_children is not None:
            input_["include_children"] = include_children

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reset_enabled_control(
        self,
        enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput":
        """<p>Resets an enabled control. Does not work for controls implemented with SCPs.</p>

        Args:
            enabled_control_identifier: <p>The ARN of the enabled control to be reset.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.reset_enabled_control_input.ResetEnabledControlInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.reset_enabled_control

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.reset_enabled_control.reset_enabled_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.reset_enabled_control_input.ResetEnabledControlInput = {}  # type: ignore[typeddict-item]
        input_["enabled_control_identifier"] = enabled_control_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnabledControlResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def create(
        self,
        control_identifier: "aws_sdk_controltower.types.control_identifier.ControlIdentifier",
        target_identifier: "aws_sdk_controltower.types.target_identifier.TargetIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        tags: Optional["aws_sdk_controltower.types.tag_map.TagMap"] = None,
        parameters: Optional[
            "aws_sdk_controltower.types.enabled_control_parameters.EnabledControlParameters"
        ] = None,
    ) -> "aws_sdk_controltower.types.enable_control_output.EnableControlOutput":
        r"""<p>This API call activates a control. It starts an asynchronous operation that creates Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            tags: <p>Tags to be applied to the <code>EnabledControl</code> resource.</p>
            parameters: <p>A list of input parameter values, which are specified to configure the control when you enable it.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.enable_control_input.EnableControlInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.enable_control_output.EnableControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.enable_control

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.enable_control.async_enable_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.enable_control_input.EnableControlInput = {}  # type: ignore[typeddict-item]
        input_["control_identifier"] = control_identifier
        input_["target_identifier"] = target_identifier
        if tags is not None:
            input_["tags"] = tags
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> (
        "aws_sdk_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
    ):
        r"""<p>Retrieves details about an enabled control. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            enabled_control_identifier: <p>The <code>controlIdentifier</code> of the enabled control.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.get_enabled_control_input.GetEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_enabled_control

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.get_enabled_control.async_get_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_enabled_control_input.GetEnabledControlInput = {}  # type: ignore[typeddict-item]
        input_["enabled_control_identifier"] = enabled_control_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        parameters: "aws_sdk_controltower.types.enabled_control_parameters.EnabledControlParameters",
        enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput":
        r"""<p> Updates the configuration of an already enabled control.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of SUCCEEDED, supply parameters that are different from the currently configured parameters. Otherwise, Amazon Web Services Control Tower will not accept the request.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of FAILED, Amazon Web Services Control Tower updates the control to match any valid parameters that you supply.</p> <p>If the <code>DriftSummary</code> status for the control shows as <code>DRIFTED</code>, you cannot call this API. Instead, you can update the control by calling the <code>ResetEnabledControl</code> API. Alternatively, you can call <code>DisableControl</code> and then call <code>EnableControl</code> again. Also, you can run an extending governance operation to repair drift. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>. </p>

        Args:
            parameters: <p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>
            enabled_control_identifier: <p> The ARN of the enabled control that will be updated. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.update_enabled_control_input.UpdateEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.update_enabled_control

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.update_enabled_control.async_update_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.update_enabled_control_input.UpdateEnabledControlInput = {}  # type: ignore[typeddict-item]
        input_["parameters"] = parameters
        input_["enabled_control_identifier"] = enabled_control_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        target_identifier: Optional[
            "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.max_results.MaxResults"
        ] = None,
        filter: Optional[
            "aws_sdk_controltower.types.enabled_control_filter.EnabledControlFilter"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "aws_sdk_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput":
        r"""<p>Lists the controls enabled by Amazon Web Services Control Tower on the specified organizational unit and the accounts it contains. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
            filter: <p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>
            include_children: <p>A boolean value that determines whether to include enabled controls from child organizational units in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.list_enabled_controls_input.ListEnabledControlsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_enabled_controls

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.list_enabled_controls.async_list_enabled_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_enabled_controls_input.ListEnabledControlsInput = {}  # type: ignore[typeddict-item]
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if include_children is not None:
            input_["include_children"] = include_children

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_enabled_control(
        self,
        enabled_control_identifier: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput":
        """<p>Resets an enabled control. Does not work for controls implemented with SCPs.</p>

        Args:
            enabled_control_identifier: <p>The ARN of the enabled control to be reset.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.reset_enabled_control_input.ResetEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.reset_enabled_control

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.reset_enabled_control.async_reset_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.reset_enabled_control_input.ResetEnabledControlInput = {}  # type: ignore[typeddict-item]
        input_["enabled_control_identifier"] = enabled_control_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
