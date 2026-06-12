from typing import TYPE_CHECKING, Optional

from aws_sdk_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.config_description
    import aws_sdk_opensearchserverless.types.config_name
    import aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options
    import aws_sdk_opensearchserverless.types.create_security_config_request
    import aws_sdk_opensearchserverless.types.create_security_config_response
    import aws_sdk_opensearchserverless.types.delete_security_config_request
    import aws_sdk_opensearchserverless.types.delete_security_config_response
    import aws_sdk_opensearchserverless.types.get_security_config_request
    import aws_sdk_opensearchserverless.types.get_security_config_response
    import aws_sdk_opensearchserverless.types.iam_federation_config_options
    import aws_sdk_opensearchserverless.types.list_security_configs_request
    import aws_sdk_opensearchserverless.types.list_security_configs_response
    import aws_sdk_opensearchserverless.types.policy_version
    import aws_sdk_opensearchserverless.types.saml_config_options
    import aws_sdk_opensearchserverless.types.security_config_id
    import aws_sdk_opensearchserverless.types.security_config_type
    import aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options
    import aws_sdk_opensearchserverless.types.update_security_config_request
    import aws_sdk_opensearchserverless.types.update_security_config_response
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class SecurityConfig:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        type: "aws_sdk_opensearchserverless.types.security_config_type.SecurityConfigType",
        name: "aws_sdk_opensearchserverless.types.config_name.ConfigName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "aws_sdk_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options: Optional[
            "aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "aws_sdk_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse":
        """<p>Specifies a security configuration for OpenSearch Serverless. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            name: <p>The name of the security configuration.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>
            iam_identity_center_options: <p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_security_config

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.create_security_config.create_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["type"] = type
        input["name"] = name
        if description is not None:
            input["description"] = description
        if saml_options is not None:
            input["saml_options"] = saml_options
        if iam_identity_center_options is not None:
            input["iam_identity_center_options"] = iam_identity_center_options
        if iam_federation_options is not None:
            input["iam_federation_options"] = iam_federation_options
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
        id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse":
        """<p>Returns information about an OpenSearch Serverless security configuration. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The unique identifier of the security configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_config

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_config.get_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId",
        config_version: "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "aws_sdk_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options_updates: Optional[
            "aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "aws_sdk_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse":
        """<p>Updates a security configuration for OpenSearch Serverless. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            config_version: <p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>SAML options in in the form of a key-value map.</p>
            iam_identity_center_options_updates: <p>Describes IAM Identity Center options in the form of a key-value map.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_config

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_config.update_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["config_version"] = config_version
        if description is not None:
            input["description"] = description
        if saml_options is not None:
            input["saml_options"] = saml_options
        if iam_identity_center_options_updates is not None:
            input["iam_identity_center_options_updates"] = (
                iam_identity_center_options_updates
            )
        if iam_federation_options is not None:
            input["iam_federation_options"] = iam_federation_options
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse":
        """<p>Deletes a security configuration for OpenSearch Serverless. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_config

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_config.delete_security_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        type: "aws_sdk_opensearchserverless.types.security_config_type.SecurityConfigType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse":
        """<p>Returns information about configured OpenSearch Serverless security configurations. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            next_token: <p>If your initial <code>ListSecurityConfigs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityConfigs</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_configs

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_configs.list_security_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest = {}  # type: ignore[typeddict-item]
        input["type"] = type
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


class AsyncSecurityConfig:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        type: "aws_sdk_opensearchserverless.types.security_config_type.SecurityConfigType",
        name: "aws_sdk_opensearchserverless.types.config_name.ConfigName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "aws_sdk_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options: Optional[
            "aws_sdk_opensearchserverless.types.create_iam_identity_center_config_options.CreateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "aws_sdk_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse":
        """<p>Specifies a security configuration for OpenSearch Serverless. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            name: <p>The name of the security configuration.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>Describes SAML options in the form of a key-value map. This field is required if you specify <code>SAML</code> for the <code>type</code> parameter.</p>
            iam_identity_center_options: <p>Describes IAM Identity Center options in the form of a key-value map. This field is required if you specify <code>iamidentitycenter</code> for the <code>type</code> parameter.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map. This field is required if you specify <code>iamFederation</code> for the <code>type</code> parameter.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_security_config_response.CreateSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_security_config

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_security_config.async_create_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.create_security_config_request.CreateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["type"] = type
        input["name"] = name
        if description is not None:
            input["description"] = description
        if saml_options is not None:
            input["saml_options"] = saml_options
        if iam_identity_center_options is not None:
            input["iam_identity_center_options"] = iam_identity_center_options
        if iam_federation_options is not None:
            input["iam_federation_options"] = iam_federation_options
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
        id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse":
        """<p>Returns information about an OpenSearch Serverless security configuration. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The unique identifier of the security configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.get_security_config_response.GetSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_config

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_config.async_get_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.get_security_config_request.GetSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId",
        config_version: "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.config_description.ConfigDescription"
        ] = None,
        saml_options: Optional[
            "aws_sdk_opensearchserverless.types.saml_config_options.SamlConfigOptions"
        ] = None,
        iam_identity_center_options_updates: Optional[
            "aws_sdk_opensearchserverless.types.update_iam_identity_center_config_options.UpdateIamIdentityCenterConfigOptions"
        ] = None,
        iam_federation_options: Optional[
            "aws_sdk_opensearchserverless.types.iam_federation_config_options.IamFederationConfigOptions"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse":
        """<p>Updates a security configuration for OpenSearch Serverless. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            config_version: <p>The version of the security configuration to be updated. You can find the most recent version of a security configuration using the <code>GetSecurityPolicy</code> command.</p>
            description: <p>A description of the security configuration.</p>
            saml_options: <p>SAML options in in the form of a key-value map.</p>
            iam_identity_center_options_updates: <p>Describes IAM Identity Center options in the form of a key-value map.</p>
            iam_federation_options: <p>Describes IAM federation options in the form of a key-value map for updating an existing security configuration. Use this field to modify IAM federation settings for the security configuration.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_security_config_response.UpdateSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_config

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_config.async_update_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.update_security_config_request.UpdateSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["config_version"] = config_version
        if description is not None:
            input["description"] = description
        if saml_options is not None:
            input["saml_options"] = saml_options
        if iam_identity_center_options_updates is not None:
            input["iam_identity_center_options_updates"] = (
                iam_identity_center_options_updates
            )
        if iam_federation_options is not None:
            input["iam_federation_options"] = iam_federation_options
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_opensearchserverless.types.security_config_id.SecurityConfigId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse":
        """<p>Deletes a security configuration for OpenSearch Serverless. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            id: <p>The security configuration identifier. For SAML the ID will be <code>saml/&lt;accountId&gt;/&lt;idpProviderName&gt;</code>. For example, <code>saml/123456789123/OKTADev</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_security_config_response.DeleteSecurityConfigResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_config

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_config.async_delete_security_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.delete_security_config_request.DeleteSecurityConfigRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        type: "aws_sdk_opensearchserverless.types.security_config_type.SecurityConfigType",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse":
        """<p>Returns information about configured OpenSearch Serverless security configurations. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html\">SAML authentication for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security configuration.</p>
            next_token: <p>If your initial <code>ListSecurityConfigs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityConfigs</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_security_configs_response.ListSecurityConfigsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_configs

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_configs.async_list_security_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.list_security_configs_request.ListSecurityConfigsRequest = {}  # type: ignore[typeddict-item]
        input["type"] = type
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
