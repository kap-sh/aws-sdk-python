from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_launch_wizard._auth._signers
import aws_sdk_launch_wizard._auth._sigv4
from aws_sdk_launch_wizard._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.create_deployment_input
    import aws_sdk_launch_wizard.types.create_deployment_output
    import aws_sdk_launch_wizard.types.delete_deployment_input
    import aws_sdk_launch_wizard.types.delete_deployment_output
    import aws_sdk_launch_wizard.types.deployment_data_summary
    import aws_sdk_launch_wizard.types.deployment_filter_list
    import aws_sdk_launch_wizard.types.deployment_id
    import aws_sdk_launch_wizard.types.deployment_name
    import aws_sdk_launch_wizard.types.deployment_pattern_name
    import aws_sdk_launch_wizard.types.deployment_pattern_version_name
    import aws_sdk_launch_wizard.types.deployment_specifications
    import aws_sdk_launch_wizard.types.get_deployment_input
    import aws_sdk_launch_wizard.types.get_deployment_output
    import aws_sdk_launch_wizard.types.list_deployments_input
    import aws_sdk_launch_wizard.types.list_deployments_output
    import aws_sdk_launch_wizard.types.max_deployment_results
    import aws_sdk_launch_wizard.types.next_token
    import aws_sdk_launch_wizard.types.tags
    import aws_sdk_launch_wizard.types.update_deployment_input
    import aws_sdk_launch_wizard.types.update_deployment_output
    import aws_sdk_launch_wizard.types.workload_name
    import aws_sdk_launch_wizard.types.workload_version_name
    from aws_sdk_launch_wizard._services.async_launch_wizard import (
        AsyncLaunchWizardClient,
        AsyncLaunchWizardClientConfig,
    )
    from aws_sdk_launch_wizard._services.launch_wizard import (
        LaunchWizardClient,
        LaunchWizardClientConfig,
    )


class Deployment:
    def __init__(self, service: LaunchWizardClient) -> None:
        self._service = service

    def create(
        self,
        workload_name: "aws_sdk_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "aws_sdk_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        name: "aws_sdk_launch_wizard.types.deployment_name.DeploymentName",
        specifications: "aws_sdk_launch_wizard.types.deployment_specifications.DeploymentSpecifications",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
        dry_run: Optional[bool] = None,
        tags: Optional["aws_sdk_launch_wizard.types.tags.Tags"] = None,
    ) -> "aws_sdk_launch_wizard.types.create_deployment_output.CreateDeploymentOutput":
        r"""<p>Creates a deployment for the given workload. Deployments created by this operation are not available in the Launch Wizard console to use the <code>Clone deployment</code> action on.</p>

        Args:
            workload_name: <p>The name of the workload. You can use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html\"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>
            deployment_pattern_name: <p>The name of the deployment pattern supported by a given workload. You can use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html\"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter. </p>
            name: <p>The name of the deployment.</p>
            specifications: <p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            tags: <p>The tags to add to the deployment.</p>

        Examples:
            Deploy a given workload with given settings.

            >>> client.create(workload_name='SAP', deployment_pattern_name='SapHanaSingle', name='TestDeployment1', dry_run=False, specifications={'DisableDeploymentRollback': 'Yes', 'SaveDeploymentArtifacts': 'No', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234566', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://xyz.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'Yes', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'})
            Deploy a given workload with given settings and passing tags for Launch Wizard deployment resource.

            >>> client.create(workload_name='SAP', deployment_pattern_name='SapHanaSingle', name='TestDeployment2', dry_run=False, specifications={'DisableDeploymentRollback': 'Yes', 'SaveDeploymentArtifacts': 'No', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234566', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://xyz.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'Yes', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'}, tags={'key1': 'val1', 'key2': 'val2'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.create_deployment_input.CreateDeploymentInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.create_deployment

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.create_deployment_input.CreateDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name
        input_["deployment_pattern_name"] = deployment_pattern_name
        input_["name"] = name
        input_["specifications"] = specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run
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
        deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "aws_sdk_launch_wizard.types.get_deployment_output.GetDeploymentOutput":
        """<p>Returns information about the deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Examples:
            Get details about a given deployment.

            >>> client.read(deployment_id='1111111-1111-1111-1111-111111111111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.get_deployment_input.GetDeploymentInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.get_deployment

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.get_deployment_input.GetDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId",
        specifications: "aws_sdk_launch_wizard.types.deployment_specifications.DeploymentSpecifications",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
        workload_version_name: Optional[
            "aws_sdk_launch_wizard.types.workload_version_name.WorkloadVersionName"
        ] = None,
        deployment_pattern_version_name: Optional[
            "aws_sdk_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
        ] = None,
        dry_run: Optional[bool] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_launch_wizard.types.update_deployment_output.UpdateDeploymentOutput":
        r"""<p>Updates a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>
            specifications: <p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>
            workload_version_name: <p>The name of the workload version.</p>
            deployment_pattern_version_name: <p>The name of the deployment pattern version.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            force: <p>Forces the update even if validation warnings are present.</p>

        Examples:
            Edit deployment specifications.

            >>> client.update(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d', specifications={'DisableDeploymentRollback': 'No', 'SaveDeploymentArtifacts': 'Yes', 'DeploymentArtifactsS3Uri': 'aws-bucket-name', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234567', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://mno.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'No', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'}, dry_run=False)
            Update deployment version.

            >>> client.update(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d', deployment_pattern_version_name='2.0.0', specifications={'DisableDeploymentRollback': 'No', 'SaveDeploymentArtifacts': 'Yes', 'DeploymentArtifactsS3Uri': 'aws-bucket-name', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234567', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://mno.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'No', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo', 'NewParameter': 'Allow'}, dry_run=False)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.update_deployment_input.UpdateDeploymentInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.update_deployment_output.UpdateDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.update_deployment

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.update_deployment.update_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.update_deployment_input.UpdateDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["deployment_id"] = deployment_id
        input_["specifications"] = specifications
        if workload_version_name is not None:
            input_["workload_version_name"] = workload_version_name
        if deployment_pattern_version_name is not None:
            input_["deployment_pattern_version_name"] = deployment_pattern_version_name
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "aws_sdk_launch_wizard.types.delete_deployment_output.DeleteDeploymentOutput":
        """<p>Deletes a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Examples:
            Delete a deployment.

            >>> client.delete(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.delete_deployment_output.DeleteDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.delete_deployment

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.delete_deployment.delete_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.delete_deployment_input.DeleteDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
        filters: Optional[
            "aws_sdk_launch_wizard.types.deployment_filter_list.DeploymentFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_launch_wizard.types.max_deployment_results.MaxDeploymentResults"
        ] = None,
        next_token: Optional["aws_sdk_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_launch_wizard.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments that have been created.</p>

        Args:
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>WORKLOAD_NAME</code> - The name used in deployments.</p> </li> <li> <p> <code>DEPLOYMENT_STATUS</code> - <code>COMPLETED</code> | <code>CREATING</code> | <code>DELETE_IN_PROGRESS</code> | <code>DELETE_INITIATING</code> | <code>DELETE_FAILED</code> | <code>DELETED</code> | <code>FAILED</code> | <code>IN_PROGRESS</code> | <code>VALIDATING</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Examples:
            List deployments in the account with filters.

            >>> client.list(filters=[{'name': 'DEPLOYMENT_STATUS', 'values': ['IN_PROGRESS']}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.list_deployments_input.ListDeploymentsInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.list_deployments

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.list_deployments_input.ListDeploymentsInput = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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


class AsyncDeployment:
    def __init__(self, service: AsyncLaunchWizardClient) -> None:
        self._service = service

    async def create(
        self,
        workload_name: "aws_sdk_launch_wizard.types.workload_name.WorkloadName",
        deployment_pattern_name: "aws_sdk_launch_wizard.types.deployment_pattern_name.DeploymentPatternName",
        name: "aws_sdk_launch_wizard.types.deployment_name.DeploymentName",
        specifications: "aws_sdk_launch_wizard.types.deployment_specifications.DeploymentSpecifications",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        dry_run: Optional[bool] = None,
        tags: Optional["aws_sdk_launch_wizard.types.tags.Tags"] = None,
    ) -> "aws_sdk_launch_wizard.types.create_deployment_output.CreateDeploymentOutput":
        r"""<p>Creates a deployment for the given workload. Deployments created by this operation are not available in the Launch Wizard console to use the <code>Clone deployment</code> action on.</p>

        Args:
            workload_name: <p>The name of the workload. You can use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html\"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>
            deployment_pattern_name: <p>The name of the deployment pattern supported by a given workload. You can use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html\"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter. </p>
            name: <p>The name of the deployment.</p>
            specifications: <p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            tags: <p>The tags to add to the deployment.</p>

        Examples:
            Deploy a given workload with given settings.

            >>> await client.create(workload_name='SAP', deployment_pattern_name='SapHanaSingle', name='TestDeployment1', dry_run=False, specifications={'DisableDeploymentRollback': 'Yes', 'SaveDeploymentArtifacts': 'No', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234566', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://xyz.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'Yes', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'})
            Deploy a given workload with given settings and passing tags for Launch Wizard deployment resource.

            >>> await client.create(workload_name='SAP', deployment_pattern_name='SapHanaSingle', name='TestDeployment2', dry_run=False, specifications={'DisableDeploymentRollback': 'Yes', 'SaveDeploymentArtifacts': 'No', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234566', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://xyz.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'Yes', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'}, tags={'key1': 'val1', 'key2': 'val2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.create_deployment_input.CreateDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.create_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.create_deployment_input.CreateDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name
        input_["deployment_pattern_name"] = deployment_pattern_name
        input_["name"] = name
        input_["specifications"] = specifications
        if dry_run is not None:
            input_["dry_run"] = dry_run
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
        deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "aws_sdk_launch_wizard.types.get_deployment_output.GetDeploymentOutput":
        """<p>Returns information about the deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Examples:
            Get details about a given deployment.

            >>> await client.read(deployment_id='1111111-1111-1111-1111-111111111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.get_deployment_input.GetDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.get_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.get_deployment_input.GetDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId",
        specifications: "aws_sdk_launch_wizard.types.deployment_specifications.DeploymentSpecifications",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        workload_version_name: Optional[
            "aws_sdk_launch_wizard.types.workload_version_name.WorkloadVersionName"
        ] = None,
        deployment_pattern_version_name: Optional[
            "aws_sdk_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
        ] = None,
        dry_run: Optional[bool] = None,
        force: Optional[bool] = None,
    ) -> "aws_sdk_launch_wizard.types.update_deployment_output.UpdateDeploymentOutput":
        r"""<p>Updates a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>
            specifications: <p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html\">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html\"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>
            workload_version_name: <p>The name of the workload version.</p>
            deployment_pattern_version_name: <p>The name of the deployment pattern version.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>
            force: <p>Forces the update even if validation warnings are present.</p>

        Examples:
            Edit deployment specifications.

            >>> await client.update(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d', specifications={'DisableDeploymentRollback': 'No', 'SaveDeploymentArtifacts': 'Yes', 'DeploymentArtifactsS3Uri': 'aws-bucket-name', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234567', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://mno.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'No', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo'}, dry_run=False)
            Update deployment version.

            >>> await client.update(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d', deployment_pattern_version_name='2.0.0', specifications={'DisableDeploymentRollback': 'No', 'SaveDeploymentArtifacts': 'Yes', 'DeploymentArtifactsS3Uri': 'aws-bucket-name', 'KeyPairName': 'keyName', 'VpcId': 'vpc-1234567', 'CreateSecurityGroup': 'No', 'ProxyServerAddress': 'http://mno.abc.com:8080', 'Timezone': 'Pacific/Wake', 'EnableEbsVolumeEncryption': 'No', 'SapSysGroupId': '5003', 'SapVirtualIPOptIn': 'No', 'SnsTopicArn': 'arn:aws:sns:us-east-1:111111222222:snsNameUsEast1.fifo', 'NewParameter': 'Allow'}, dry_run=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.update_deployment_input.UpdateDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.update_deployment_output.UpdateDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.update_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.update_deployment.async_update_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.update_deployment_input.UpdateDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["deployment_id"] = deployment_id
        input_["specifications"] = specifications
        if workload_version_name is not None:
            input_["workload_version_name"] = workload_version_name
        if deployment_pattern_version_name is not None:
            input_["deployment_pattern_version_name"] = deployment_pattern_version_name
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        deployment_id: "aws_sdk_launch_wizard.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "aws_sdk_launch_wizard.types.delete_deployment_output.DeleteDeploymentOutput":
        """<p>Deletes a deployment.</p>

        Args:
            deployment_id: <p>The ID of the deployment.</p>

        Examples:
            Delete a deployment.

            >>> await client.delete(deployment_id='4c1b59c1-659c-467f-b6e9-6ef6f9d28e1d')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.delete_deployment_output.DeleteDeploymentOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.delete_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.delete_deployment_input.DeleteDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        filters: Optional[
            "aws_sdk_launch_wizard.types.deployment_filter_list.DeploymentFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_launch_wizard.types.max_deployment_results.MaxDeploymentResults"
        ] = None,
        next_token: Optional["aws_sdk_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_launch_wizard.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments that have been created.</p>

        Args:
            filters: <p>Filters to scope the results. The following filters are supported:</p> <ul> <li> <p> <code>WORKLOAD_NAME</code> - The name used in deployments.</p> </li> <li> <p> <code>DEPLOYMENT_STATUS</code> - <code>COMPLETED</code> | <code>CREATING</code> | <code>DELETE_IN_PROGRESS</code> | <code>DELETE_INITIATING</code> | <code>DELETE_FAILED</code> | <code>DELETED</code> | <code>FAILED</code> | <code>IN_PROGRESS</code> | <code>VALIDATING</code> </p> </li> </ul>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Examples:
            List deployments in the account with filters.

            >>> await client.list(filters=[{'name': 'DEPLOYMENT_STATUS', 'values': ['IN_PROGRESS']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.list_deployments_input.ListDeploymentsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.list_deployments

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.list_deployments_input.ListDeploymentsInput = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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
