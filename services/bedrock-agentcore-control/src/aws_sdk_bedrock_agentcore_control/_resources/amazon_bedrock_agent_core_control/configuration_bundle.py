from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
from aws_sdk_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.branch_name
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.component_configuration_map
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary
    import aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_request
    import aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_response
    import aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_request
    import aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_response
    import aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_request
    import aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_response
    import aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_request
    import aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_response
    import aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_request
    import aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_response
    import aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_request
    import aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_response
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_request
    import aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_response
    import aws_sdk_bedrock_agentcore_control.types.version_created_by_source
    import aws_sdk_bedrock_agentcore_control.types.version_filter
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class ConfigurationBundle:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        bundle_name: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName",
        components: "aws_sdk_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
        ] = None,
        branch_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
        commit_message: Optional[str] = None,
        created_by: Optional[
            "aws_sdk_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_response.CreateConfigurationBundleResponse":
        r"""<p>Creates a new configuration bundle resource. A configuration bundle stores versioned component configurations for agent evaluation workflows.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            bundle_name: <p>The name for the configuration bundle. Names must be unique within your account.</p>
            description: <p>The description for the configuration bundle.</p>
            components: <p>A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.</p>
            branch_name: <p>The branch name for version tracking. Defaults to <code>mainline</code> if not specified.</p>
            commit_message: <p>A commit message describing the initial version of the configuration bundle.</p>
            created_by: <p>The source that created this version, including the source name and optional ARN.</p>
            tags: <p>A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_request.CreateConfigurationBundleRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_response.CreateConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_configuration_bundle

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_configuration_bundle.create_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_request.CreateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["bundle_name"] = bundle_name
        if description is not None:
            input_["description"] = description
        input_["components"] = components
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if created_by is not None:
            input_["created_by"] = created_by
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
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        branch_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_response.GetConfigurationBundleResponse":
        """<p>Gets the latest version of a configuration bundle. By default, returns the latest version on the mainline branch. Use <code>GetConfigurationBundleVersion</code> to retrieve a specific historical version.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to retrieve.</p>
            branch_name: <p>The branch name to get the latest version from. If not specified, returns the latest version on the mainline branch.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_request.GetConfigurationBundleRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_response.GetConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle.get_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_request.GetConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        if branch_name is not None:
            input_["branch_name"] = branch_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        bundle_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
        ] = None,
        components: Optional[
            "aws_sdk_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
        ] = None,
        parent_version_ids: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list.ConfigurationBundleVersionList"
        ] = None,
        branch_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
        commit_message: Optional[str] = None,
        created_by: Optional[
            "aws_sdk_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_response.UpdateConfigurationBundleResponse":
        r"""<p>Updates a configuration bundle by creating a new version with the specified changes. Each update creates a new version in the version history.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            bundle_id: <p>The unique identifier of the configuration bundle to update.</p>
            bundle_name: <p>The updated name for the configuration bundle.</p>
            description: <p>The updated description for the configuration bundle.</p>
            components: <p>The updated component configurations. Creates a new version of the bundle.</p>
            parent_version_ids: <p>A list of parent version identifiers for lineage tracking. Regular commits have a single parent. Merge commits have two parents: the target branch parent and the source branch parent. If the branch already exists, the first parent must be the latest version on that branch.</p>
            branch_name: <p>The branch name for this version. If not specified, inherits the parent's branch or defaults to <code>mainline</code>.</p>
            commit_message: <p>A commit message describing the changes in this version.</p>
            created_by: <p>The source that created this version, including the source name and optional ARN.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_request.UpdateConfigurationBundleRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_response.UpdateConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_configuration_bundle

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_configuration_bundle.update_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_request.UpdateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["bundle_id"] = bundle_id
        if bundle_name is not None:
            input_["bundle_name"] = bundle_name
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if parent_version_ids is not None:
            input_["parent_version_ids"] = parent_version_ids
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if created_by is not None:
            input_["created_by"] = created_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_response.DeleteConfigurationBundleResponse":
        """<p>Deletes a configuration bundle and all of its versions.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to delete.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_request.DeleteConfigurationBundleRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_response.DeleteConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_configuration_bundle

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_configuration_bundle.delete_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_request.DeleteConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_response.ListConfigurationBundlesResponse":
        """<p>Lists all configuration bundles in the account.</p>

        Args:
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_request.ListConfigurationBundlesRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_response.ListConfigurationBundlesResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundles

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundles.list_configuration_bundles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_request.ListConfigurationBundlesRequest = {}  # type: ignore[typeddict-item]
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

    def get_configuration_bundle_version(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        version_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_response.GetConfigurationBundleVersionResponse":
        """<p>Gets a specific version of a configuration bundle by its version identifier.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle.</p>
            version_id: <p>The version identifier of the configuration bundle version to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_request.GetConfigurationBundleVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_response.GetConfigurationBundleVersionResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle_version

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle_version.get_configuration_bundle_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_request.GetConfigurationBundleVersionRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_configuration_bundle_versions(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "aws_sdk_bedrock_agentcore_control.types.version_filter.VersionFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_response.ListConfigurationBundleVersionsResponse":
        """<p>Lists all versions of a configuration bundle, with optional filtering by branch name or creation source.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to list versions for.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            filter: <p>An optional filter for listing versions, including branch name, creation source, and whether to return only the latest version per branch.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_request.ListConfigurationBundleVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_response.ListConfigurationBundleVersionsResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundle_versions

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundle_versions.list_configuration_bundle_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_request.ListConfigurationBundleVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConfigurationBundle:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        bundle_name: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName",
        components: "aws_sdk_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
        ] = None,
        branch_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
        commit_message: Optional[str] = None,
        created_by: Optional[
            "aws_sdk_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_response.CreateConfigurationBundleResponse":
        r"""<p>Creates a new configuration bundle resource. A configuration bundle stores versioned component configurations for agent evaluation workflows.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            bundle_name: <p>The name for the configuration bundle. Names must be unique within your account.</p>
            description: <p>The description for the configuration bundle.</p>
            components: <p>A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.</p>
            branch_name: <p>The branch name for version tracking. Defaults to <code>mainline</code> if not specified.</p>
            commit_message: <p>A commit message describing the initial version of the configuration bundle.</p>
            created_by: <p>The source that created this version, including the source name and optional ARN.</p>
            tags: <p>A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_request.CreateConfigurationBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_response.CreateConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_configuration_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_configuration_bundle.async_create_configuration_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_configuration_bundle_request.CreateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["bundle_name"] = bundle_name
        if description is not None:
            input_["description"] = description
        input_["components"] = components
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if created_by is not None:
            input_["created_by"] = created_by
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
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        branch_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_response.GetConfigurationBundleResponse":
        """<p>Gets the latest version of a configuration bundle. By default, returns the latest version on the mainline branch. Use <code>GetConfigurationBundleVersion</code> to retrieve a specific historical version.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to retrieve.</p>
            branch_name: <p>The branch name to get the latest version from. If not specified, returns the latest version on the mainline branch.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_request.GetConfigurationBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_response.GetConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle.async_get_configuration_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_request.GetConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        if branch_name is not None:
            input_["branch_name"] = branch_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        bundle_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
        ] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
        ] = None,
        components: Optional[
            "aws_sdk_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
        ] = None,
        parent_version_ids: Optional[
            "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_list.ConfigurationBundleVersionList"
        ] = None,
        branch_name: Optional[
            "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
        commit_message: Optional[str] = None,
        created_by: Optional[
            "aws_sdk_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_response.UpdateConfigurationBundleResponse":
        r"""<p>Updates a configuration bundle by creating a new version with the specified changes. Each update creates a new version in the version history.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            bundle_id: <p>The unique identifier of the configuration bundle to update.</p>
            bundle_name: <p>The updated name for the configuration bundle.</p>
            description: <p>The updated description for the configuration bundle.</p>
            components: <p>The updated component configurations. Creates a new version of the bundle.</p>
            parent_version_ids: <p>A list of parent version identifiers for lineage tracking. Regular commits have a single parent. Merge commits have two parents: the target branch parent and the source branch parent. If the branch already exists, the first parent must be the latest version on that branch.</p>
            branch_name: <p>The branch name for this version. If not specified, inherits the parent's branch or defaults to <code>mainline</code>.</p>
            commit_message: <p>A commit message describing the changes in this version.</p>
            created_by: <p>The source that created this version, including the source name and optional ARN.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_request.UpdateConfigurationBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_response.UpdateConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_configuration_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_configuration_bundle.async_update_configuration_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_configuration_bundle_request.UpdateConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["bundle_id"] = bundle_id
        if bundle_name is not None:
            input_["bundle_name"] = bundle_name
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if parent_version_ids is not None:
            input_["parent_version_ids"] = parent_version_ids
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if created_by is not None:
            input_["created_by"] = created_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_response.DeleteConfigurationBundleResponse":
        """<p>Deletes a configuration bundle and all of its versions.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to delete.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_request.DeleteConfigurationBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_response.DeleteConfigurationBundleResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_configuration_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_configuration_bundle.async_delete_configuration_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_configuration_bundle_request.DeleteConfigurationBundleRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_response.ListConfigurationBundlesResponse":
        """<p>Lists all configuration bundles in the account.</p>

        Args:
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_request.ListConfigurationBundlesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_response.ListConfigurationBundlesResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundles

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundles.async_list_configuration_bundles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_configuration_bundles_request.ListConfigurationBundlesRequest = {}  # type: ignore[typeddict-item]
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

    async def get_configuration_bundle_version(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        version_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_response.GetConfigurationBundleVersionResponse":
        """<p>Gets a specific version of a configuration bundle by its version identifier.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle.</p>
            version_id: <p>The version identifier of the configuration bundle version to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_request.GetConfigurationBundleVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_response.GetConfigurationBundleVersionResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle_version

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle_version.async_get_configuration_bundle_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_configuration_bundle_version_request.GetConfigurationBundleVersionRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        input_["version_id"] = version_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_configuration_bundle_versions(
        self,
        bundle_id: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "aws_sdk_bedrock_agentcore_control.types.version_filter.VersionFilter"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_response.ListConfigurationBundleVersionsResponse":
        """<p>Lists all versions of a configuration bundle, with optional filtering by branch name or creation source.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to list versions for.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            filter: <p>An optional filter for listing versions, including branch name, creation source, and whether to return only the latest version per branch.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_request.ListConfigurationBundleVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_response.ListConfigurationBundleVersionsResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundle_versions

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundle_versions.async_list_configuration_bundle_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_configuration_bundle_versions_request.ListConfigurationBundleVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["bundle_id"] = bundle_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
