from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanrooms._auth._signers
import aws_sdk_cleanrooms._auth._sigv4
from aws_sdk_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_format
    import aws_sdk_cleanrooms.types.analysis_parameter_list
    import aws_sdk_cleanrooms.types.analysis_schema
    import aws_sdk_cleanrooms.types.analysis_source
    import aws_sdk_cleanrooms.types.analysis_template_identifier
    import aws_sdk_cleanrooms.types.create_analysis_template_input
    import aws_sdk_cleanrooms.types.create_analysis_template_output
    import aws_sdk_cleanrooms.types.delete_analysis_template_input
    import aws_sdk_cleanrooms.types.delete_analysis_template_output
    import aws_sdk_cleanrooms.types.error_message_configuration
    import aws_sdk_cleanrooms.types.get_analysis_template_input
    import aws_sdk_cleanrooms.types.get_analysis_template_output
    import aws_sdk_cleanrooms.types.list_analysis_templates_input
    import aws_sdk_cleanrooms.types.list_analysis_templates_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.synthetic_data_parameters
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_analysis_template_input
    import aws_sdk_cleanrooms.types.update_analysis_template_output
    from aws_sdk_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from aws_sdk_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class AnalysisTemplateResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "aws_sdk_cleanrooms.types.table_alias.TableAlias",
        format: "aws_sdk_cleanrooms.types.analysis_format.AnalysisFormat",
        source: "aws_sdk_cleanrooms.types.analysis_source.AnalysisSource",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        analysis_parameters: Optional[
            "aws_sdk_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
        ] = None,
        schema: Optional[
            "aws_sdk_cleanrooms.types.analysis_schema.AnalysisSchema"
        ] = None,
        error_message_configuration: Optional[
            "aws_sdk_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
        ] = None,
        synthetic_data_parameters: Optional[
            "aws_sdk_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput":
        """<p>Creates a new analysis template.</p>

        Args:
            description: <p>The description of the analysis template.</p>
            membership_identifier: <p>The identifier for a membership resource.</p>
            name: <p>The name of the analysis template.</p>
            format: <p>The format of the analysis template.</p>
            source: <p>The information in the analysis template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            analysis_parameters: <p>The parameters of the analysis template.</p>
            error_message_configuration: <p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>
            synthetic_data_parameters: <p>The parameters for generating synthetic data when running the analysis template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template.create_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["membership_identifier"] = membership_identifier
        input_["name"] = name
        input_["format"] = format
        input_["source"] = source
        if tags is not None:
            input_["tags"] = tags
        if analysis_parameters is not None:
            input_["analysis_parameters"] = analysis_parameters
        if schema is not None:
            input_["schema"] = schema
        if error_message_configuration is not None:
            input_["error_message_configuration"] = error_message_configuration
        if synthetic_data_parameters is not None:
            input_["synthetic_data_parameters"] = synthetic_data_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput":
        """<p>Retrieves an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template.get_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["analysis_template_identifier"] = analysis_template_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput":
        """<p>Updates the analysis template metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
            description: <p>A new description for the analysis template.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template.update_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["analysis_template_identifier"] = analysis_template_identifier
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput":
        """<p>Deletes an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template.delete_analysis_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["analysis_template_identifier"] = analysis_template_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput":
        """<p>Lists analysis templates that the caller owns.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates.list_analysis_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAnalysisTemplateResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        name: "aws_sdk_cleanrooms.types.table_alias.TableAlias",
        format: "aws_sdk_cleanrooms.types.analysis_format.AnalysisFormat",
        source: "aws_sdk_cleanrooms.types.analysis_source.AnalysisSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        analysis_parameters: Optional[
            "aws_sdk_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
        ] = None,
        schema: Optional[
            "aws_sdk_cleanrooms.types.analysis_schema.AnalysisSchema"
        ] = None,
        error_message_configuration: Optional[
            "aws_sdk_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
        ] = None,
        synthetic_data_parameters: Optional[
            "aws_sdk_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput":
        """<p>Creates a new analysis template.</p>

        Args:
            description: <p>The description of the analysis template.</p>
            membership_identifier: <p>The identifier for a membership resource.</p>
            name: <p>The name of the analysis template.</p>
            format: <p>The format of the analysis template.</p>
            source: <p>The information in the analysis template.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            analysis_parameters: <p>The parameters of the analysis template.</p>
            error_message_configuration: <p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>
            synthetic_data_parameters: <p>The parameters for generating synthetic data when running the analysis template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_analysis_template_output.CreateAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_analysis_template.async_create_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_analysis_template_input.CreateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["membership_identifier"] = membership_identifier
        input_["name"] = name
        input_["format"] = format
        input_["source"] = source
        if tags is not None:
            input_["tags"] = tags
        if analysis_parameters is not None:
            input_["analysis_parameters"] = analysis_parameters
        if schema is not None:
            input_["schema"] = schema
        if error_message_configuration is not None:
            input_["error_message_configuration"] = error_message_configuration
        if synthetic_data_parameters is not None:
            input_["synthetic_data_parameters"] = synthetic_data_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput":
        """<p>Retrieves an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_analysis_template_output.GetAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_analysis_template.async_get_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_analysis_template_input.GetAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["analysis_template_identifier"] = analysis_template_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput":
        """<p>Updates the analysis template metadata.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
            description: <p>A new description for the analysis template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_analysis_template_output.UpdateAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_analysis_template.async_update_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_analysis_template_input.UpdateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["analysis_template_identifier"] = analysis_template_identifier
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        analysis_template_identifier: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput":
        """<p>Deletes an analysis template.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            analysis_template_identifier: <p>The identifier for the analysis template resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_analysis_template_output.DeleteAnalysisTemplateOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_analysis_template.async_delete_analysis_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_analysis_template_input.DeleteAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["analysis_template_identifier"] = analysis_template_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput":
        """<p>Lists analysis templates that the caller owns.</p>

        Args:
            membership_identifier: <p>The identifier for a membership resource.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_analysis_templates_output.ListAnalysisTemplatesOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_analysis_templates.async_list_analysis_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_analysis_templates_input.ListAnalysisTemplatesInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
