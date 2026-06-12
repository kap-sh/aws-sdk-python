from typing import Optional, TYPE_CHECKING
from aws_sdk_braket._services.async_braket import ensure_async_iterator
from aws_sdk_braket._services.braket import ensure_sync_iterator
from aws_sdk_braket._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_braket._auth._signers
import aws_sdk_braket._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_braket._services.braket import BraketClient, BraketClientConfig
    from aws_sdk_braket._services.async_braket import AsyncBraketClient, AsyncBraketClientConfig
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.device_summary
    import aws_sdk_braket.types.get_device_request
    import aws_sdk_braket.types.get_device_response
    import aws_sdk_braket.types.search_devices_filter_list
    import aws_sdk_braket.types.search_devices_request
    import aws_sdk_braket.types.search_devices_response

class DeviceResource:
    def __init__(self, service: BraketClient) -> None:
        self._service = service
    def read(self, device_arn: "aws_sdk_braket.types.device_arn.DeviceArn", *, config_overrides: Optional[BraketClientConfig] = None) -> "aws_sdk_braket.types.get_device_response.GetDeviceResponse":
        """<p>Retrieves the devices available in Amazon Braket.</p> <note> <p>For backwards compatibility with older versions of BraketSchemas, OpenQASM information is omitted from GetDevice API calls. To get this information the user-agent needs to present a recent version of the BraketSchemas (1.8.0 or later). The Braket SDK automatically reports this for you. If you do not see OpenQASM results in the GetDevice response when using a Braket SDK, you may need to set AWS_EXECUTION_ENV environment variable to configure user-agent. See the code examples provided below for how to do this for the AWS CLI, Boto3, and the Go, Java, and JavaScript/TypeScript SDKs.</p> </note>

        Args:
            device_arn: <p>The ARN of the device to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_braket.types.get_device_request.GetDeviceRequest]') -> OperationResponse["aws_sdk_braket.types.get_device_response.GetDeviceResponse"]:
            import aws_sdk_braket._operations.braket.get_device
            output, http_response = aws_sdk_braket._operations.braket.get_device.get_device(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.get_device_request.GetDeviceRequest = {}  # type: ignore[typeddict-item]
        input["device_arn"] = device_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, filters: "aws_sdk_braket.types.search_devices_filter_list.SearchDevicesFilterList", *, config_overrides: Optional[BraketClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_braket.types.search_devices_response.SearchDevicesResponse":
        """<p>Searches for devices using the specified filters.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchDevicesFilter objects to use when searching for devices.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_braket.types.search_devices_request.SearchDevicesRequest]') -> OperationResponse["aws_sdk_braket.types.search_devices_response.SearchDevicesResponse"]:
            import aws_sdk_braket._operations.braket.search_devices
            output, http_response = aws_sdk_braket._operations.braket.search_devices.search_devices(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_devices_request.SearchDevicesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["filters"] = filters

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncDeviceResource:
    def __init__(self, service: AsyncBraketClient) -> None:
        self._service = service
    async def read(self, device_arn: "aws_sdk_braket.types.device_arn.DeviceArn", *, config_overrides: Optional[AsyncBraketClientConfig] = None) -> "aws_sdk_braket.types.get_device_response.GetDeviceResponse":
        """<p>Retrieves the devices available in Amazon Braket.</p> <note> <p>For backwards compatibility with older versions of BraketSchemas, OpenQASM information is omitted from GetDevice API calls. To get this information the user-agent needs to present a recent version of the BraketSchemas (1.8.0 or later). The Braket SDK automatically reports this for you. If you do not see OpenQASM results in the GetDevice response when using a Braket SDK, you may need to set AWS_EXECUTION_ENV environment variable to configure user-agent. See the code examples provided below for how to do this for the AWS CLI, Boto3, and the Go, Java, and JavaScript/TypeScript SDKs.</p> </note>

        Args:
            device_arn: <p>The ARN of the device to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_braket.types.get_device_request.GetDeviceRequest]') -> AsyncOperationResponse["aws_sdk_braket.types.get_device_response.GetDeviceResponse"]:
            import aws_sdk_braket._operations.braket.get_device
            output, http_response = await aws_sdk_braket._operations.braket.get_device.async_get_device(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.get_device_request.GetDeviceRequest = {}  # type: ignore[typeddict-item]
        input["device_arn"] = device_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, filters: "aws_sdk_braket.types.search_devices_filter_list.SearchDevicesFilterList", *, config_overrides: Optional[AsyncBraketClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_braket.types.search_devices_response.SearchDevicesResponse":
        """<p>Searches for devices using the specified filters.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchDevicesFilter objects to use when searching for devices.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_braket.types.search_devices_request.SearchDevicesRequest]') -> AsyncOperationResponse["aws_sdk_braket.types.search_devices_response.SearchDevicesResponse"]:
            import aws_sdk_braket._operations.braket.search_devices
            output, http_response = await aws_sdk_braket._operations.braket.search_devices.async_search_devices(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_devices_request.SearchDevicesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["filters"] = filters

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output