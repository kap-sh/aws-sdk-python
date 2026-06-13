from typing import TYPE_CHECKING, Optional

from aws_sdk_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_proton.types.deployment_update_type
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.spec_contents
    import aws_sdk_proton.types.template_version_part
    import aws_sdk_proton.types.update_service_pipeline_input
    import aws_sdk_proton.types.update_service_pipeline_output
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class ServicePipelineResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def update(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        spec: "aws_sdk_proton.types.spec_contents.SpecContents",
        deployment_type: "aws_sdk_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        template_major_version: Optional[
            "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "aws_sdk_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput":
        """<p>Update the service pipeline.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            service_name: <p>The name of the service to that the pipeline is associated with.</p>
            spec: <p>The spec for the service pipeline to update.</p>
            deployment_type: <p>The deployment type.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            template_major_version: <p>The major version of the service template that was used to create the service that the pipeline is associated with.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service that the pipeline is associated with.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.update_service_pipeline_input.UpdateServicePipelineInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_pipeline

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.update_service_pipeline.update_service_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_pipeline_input.UpdateServicePipelineInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name
        input["spec"] = spec
        input["deployment_type"] = deployment_type
        if template_major_version is not None:
            input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServicePipelineResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def update(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        spec: "aws_sdk_proton.types.spec_contents.SpecContents",
        deployment_type: "aws_sdk_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        template_major_version: Optional[
            "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "aws_sdk_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "aws_sdk_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput":
        """<p>Update the service pipeline.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            service_name: <p>The name of the service to that the pipeline is associated with.</p>
            spec: <p>The spec for the service pipeline to update.</p>
            deployment_type: <p>The deployment type.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            template_major_version: <p>The major version of the service template that was used to create the service that the pipeline is associated with.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service that the pipeline is associated with.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.update_service_pipeline_input.UpdateServicePipelineInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_pipeline

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.update_service_pipeline.async_update_service_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_proton.types.update_service_pipeline_input.UpdateServicePipelineInput = {}  # type: ignore[typeddict-item]
        input["service_name"] = service_name
        input["spec"] = spec
        input["deployment_type"] = deployment_type
        if template_major_version is not None:
            input["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input["template_minor_version"] = template_minor_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
