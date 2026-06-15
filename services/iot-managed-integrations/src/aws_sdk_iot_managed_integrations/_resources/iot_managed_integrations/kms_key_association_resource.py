from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.encryption_type
    import aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_request
    import aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_response
    import aws_sdk_iot_managed_integrations.types.kms_key_arn
    import aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_request
    import aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_response
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class KmsKeyAssociationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def get_default_encryption_configuration(
        self, *, config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None
    ) -> "aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse":
        r"""<p> Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified region. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the <i>AWS IoT SiteWise User Guide</i>.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration.get_default_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_default_encryption_configuration(
        self,
        encryption_type: "aws_sdk_iot_managed_integrations.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        kms_key_arn: Optional[
            "aws_sdk_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        r"""<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the AWS IoT SiteWise User Guide.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_arn: <p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration.put_default_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["encryption_type"] = encryption_type
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncKmsKeyAssociationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def get_default_encryption_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse":
        r"""<p> Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified region. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the <i>AWS IoT SiteWise User Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration.async_get_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_default_encryption_configuration(
        self,
        encryption_type: "aws_sdk_iot_managed_integrations.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        kms_key_arn: Optional[
            "aws_sdk_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        r"""<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the AWS IoT SiteWise User Guide.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_arn: <p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration.async_put_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["encryption_type"] = encryption_type
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
