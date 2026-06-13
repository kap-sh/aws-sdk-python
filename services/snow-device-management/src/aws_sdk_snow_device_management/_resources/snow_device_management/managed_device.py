from typing import TYPE_CHECKING, Optional

import aws_sdk_snow_device_management._auth._signers
import aws_sdk_snow_device_management._auth._sigv4
from aws_sdk_snow_device_management._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.describe_device_ec2_input
    import aws_sdk_snow_device_management.types.describe_device_ec2_output
    import aws_sdk_snow_device_management.types.describe_device_input
    import aws_sdk_snow_device_management.types.describe_device_output
    import aws_sdk_snow_device_management.types.device_summary
    import aws_sdk_snow_device_management.types.instance_ids_list
    import aws_sdk_snow_device_management.types.job_id
    import aws_sdk_snow_device_management.types.list_device_resources_input
    import aws_sdk_snow_device_management.types.list_device_resources_output
    import aws_sdk_snow_device_management.types.list_devices_input
    import aws_sdk_snow_device_management.types.list_devices_output
    import aws_sdk_snow_device_management.types.managed_device_id
    import aws_sdk_snow_device_management.types.max_results
    import aws_sdk_snow_device_management.types.next_token
    import aws_sdk_snow_device_management.types.resource_summary
    from aws_sdk_snow_device_management._services.async_snow_device_management import (
        AsyncSnowDeviceManagementClient,
        AsyncSnowDeviceManagementClientConfig,
    )
    from aws_sdk_snow_device_management._services.snow_device_management import (
        SnowDeviceManagementClient,
        SnowDeviceManagementClientConfig,
    )


class ManagedDevice:
    def __init__(self, service: SnowDeviceManagementClient) -> None:
        self._service = service

    def read(
        self,
        managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.describe_device_output.DescribeDeviceOutput":
        """<p>Checks device-specific information, such as the device type, software version, IP addresses, and lock status.</p>

        Args:
            managed_device_id: <p>The ID of the device that you are checking the information of.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.describe_device_input.DescribeDeviceInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.describe_device

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.describe_device.describe_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.describe_device_input.DescribeDeviceInput = {}  # type: ignore[typeddict-item]
        input["managed_device_id"] = managed_device_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        job_id: Optional["aws_sdk_snow_device_management.types.job_id.JobId"] = None,
        max_results: Optional[
            "aws_sdk_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.list_devices_output.ListDevicesOutput":
        """<p>Returns a list of all devices on your Amazon Web Services account that have Amazon Web Services Snow Device Management enabled in the Amazon Web Services Region where the command is run.</p>

        Args:
            job_id: <p>The ID of the job used to order the device.</p>
            max_results: <p>The maximum number of devices to list per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.list_devices_input.ListDevicesInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.list_devices_output.ListDevicesOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_devices

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.list_devices.list_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.list_devices_input.ListDevicesInput = {}  # type: ignore[typeddict-item]
        if job_id is not None:
            input["job_id"] = job_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_device_ec2_instances(
        self,
        managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId",
        instance_ids: "aws_sdk_snow_device_management.types.instance_ids_list.InstanceIdsList",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output":
        """<p>Checks the current state of the Amazon EC2 instances. The output is similar to <code>describeDevice</code>, but the results are sourced from the device cache in the Amazon Web Services Cloud and include a subset of the available fields. </p>

        Args:
            managed_device_id: <p>The ID of the managed device.</p>
            instance_ids: <p>A list of instance IDs associated with the managed device.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.describe_device_ec2_instances

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.describe_device_ec2_instances.describe_device_ec2_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input = {}  # type: ignore[typeddict-item]
        input["managed_device_id"] = managed_device_id
        input["instance_ids"] = instance_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_device_resources(
        self,
        managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        type: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput":
        """<p>Returns a list of the Amazon Web Services resources available for a device. Currently, Amazon EC2 instances are the only supported resource type.</p>

        Args:
            managed_device_id: <p>The ID of the managed device that you are listing the resources of.</p>
            type: <p>A structure used to filter the results by type of resource.</p>
            max_results: <p>The maximum number of resources per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_device_resources

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.list_device_resources.list_device_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput = {}  # type: ignore[typeddict-item]
        input["managed_device_id"] = managed_device_id
        if type is not None:
            input["type"] = type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedDevice:
    def __init__(self, service: AsyncSnowDeviceManagementClient) -> None:
        self._service = service

    async def read(
        self,
        managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.describe_device_output.DescribeDeviceOutput":
        """<p>Checks device-specific information, such as the device type, software version, IP addresses, and lock status.</p>

        Args:
            managed_device_id: <p>The ID of the device that you are checking the information of.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.describe_device_input.DescribeDeviceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.describe_device

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.describe_device.async_describe_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.describe_device_input.DescribeDeviceInput = {}  # type: ignore[typeddict-item]
        input["managed_device_id"] = managed_device_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        job_id: Optional["aws_sdk_snow_device_management.types.job_id.JobId"] = None,
        max_results: Optional[
            "aws_sdk_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.list_devices_output.ListDevicesOutput":
        """<p>Returns a list of all devices on your Amazon Web Services account that have Amazon Web Services Snow Device Management enabled in the Amazon Web Services Region where the command is run.</p>

        Args:
            job_id: <p>The ID of the job used to order the device.</p>
            max_results: <p>The maximum number of devices to list per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.list_devices_input.ListDevicesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.list_devices_output.ListDevicesOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_devices

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.list_devices.async_list_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.list_devices_input.ListDevicesInput = {}  # type: ignore[typeddict-item]
        if job_id is not None:
            input["job_id"] = job_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_device_ec2_instances(
        self,
        managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId",
        instance_ids: "aws_sdk_snow_device_management.types.instance_ids_list.InstanceIdsList",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output":
        """<p>Checks the current state of the Amazon EC2 instances. The output is similar to <code>describeDevice</code>, but the results are sourced from the device cache in the Amazon Web Services Cloud and include a subset of the available fields. </p>

        Args:
            managed_device_id: <p>The ID of the managed device.</p>
            instance_ids: <p>A list of instance IDs associated with the managed device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.describe_device_ec2_instances

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.describe_device_ec2_instances.async_describe_device_ec2_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input = {}  # type: ignore[typeddict-item]
        input["managed_device_id"] = managed_device_id
        input["instance_ids"] = instance_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_device_resources(
        self,
        managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        type: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput":
        """<p>Returns a list of the Amazon Web Services resources available for a device. Currently, Amazon EC2 instances are the only supported resource type.</p>

        Args:
            managed_device_id: <p>The ID of the managed device that you are listing the resources of.</p>
            type: <p>A structure used to filter the results by type of resource.</p>
            max_results: <p>The maximum number of resources per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_device_resources

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.list_device_resources.async_list_device_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput = {}  # type: ignore[typeddict-item]
        input["managed_device_id"] = managed_device_id
        if type is not None:
            input["type"] = type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
