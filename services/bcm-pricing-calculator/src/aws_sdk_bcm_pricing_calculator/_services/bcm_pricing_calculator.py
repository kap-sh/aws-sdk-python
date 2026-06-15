"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#AWSBCMPricingCalculator``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_bcm_pricing_calculator._auth._signers
import aws_sdk_bcm_pricing_calculator._auth._sigv4
from aws_sdk_bcm_pricing_calculator._auth._identity import Credentials
from aws_sdk_bcm_pricing_calculator._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bcm_pricing_calculator._auth._zapros_handler import AuthMiddleware
from aws_sdk_bcm_pricing_calculator._resources.awsbcm_pricing_calculator.bill_estimate import (
    BillEstimate,
)
from aws_sdk_bcm_pricing_calculator._resources.awsbcm_pricing_calculator.bill_scenario import (
    BillScenario,
)
from aws_sdk_bcm_pricing_calculator._resources.awsbcm_pricing_calculator.workload_estimate import (
    WorkloadEstimate,
)
from aws_sdk_bcm_pricing_calculator._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.arn
    import aws_sdk_bcm_pricing_calculator.types.get_preferences_request
    import aws_sdk_bcm_pricing_calculator.types.get_preferences_response
    import aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_request
    import aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_response
    import aws_sdk_bcm_pricing_calculator.types.rate_types
    import aws_sdk_bcm_pricing_calculator.types.resource_tag_keys
    import aws_sdk_bcm_pricing_calculator.types.tag_resource_request
    import aws_sdk_bcm_pricing_calculator.types.tag_resource_response
    import aws_sdk_bcm_pricing_calculator.types.tags
    import aws_sdk_bcm_pricing_calculator.types.untag_resource_request
    import aws_sdk_bcm_pricing_calculator.types.untag_resource_response
    import aws_sdk_bcm_pricing_calculator.types.update_preferences_request
    import aws_sdk_bcm_pricing_calculator.types.update_preferences_response


class BCMPricingCalculatorClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class BCMPricingCalculatorClient:
    """A client for the ``BCMPricingCalculator`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = BCMPricingCalculatorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.bill_estimate = BillEstimate(self)
        self.bill_scenario = BillScenario(self)
        self.workload_estimate = WorkloadEstimate(self)

    def operation_options(
        self, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BCMPricingCalculatorClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_preferences(
        self, *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None
    ) -> "aws_sdk_bcm_pricing_calculator.types.get_preferences_response.GetPreferencesResponse":
        """<p> Retrieves the current preferences for Pricing Calculator. </p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.get_preferences_request.GetPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.get_preferences_response.GetPreferencesResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_preferences

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_preferences.get_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_pricing_calculator.types.get_preferences_request.GetPreferencesRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Lists all tags associated with a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to list tags for. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_tags_for_resource

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn",
        tags: "aws_sdk_bcm_pricing_calculator.types.tags.Tags",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> (
        "aws_sdk_bcm_pricing_calculator.types.tag_resource_response.TagResourceResponse"
    ):
        """<p> Adds one or more tags to a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to add tags to. </p>
            tags: <p> The tags to add to the resource. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.tag_resource

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_pricing_calculator.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn",
        tag_keys: "aws_sdk_bcm_pricing_calculator.types.resource_tag_keys.ResourceTagKeys",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to remove tags from. </p>
            tag_keys: <p> The keys of the tags to remove from the resource. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.untag_resource

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_pricing_calculator.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_preferences(
        self,
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        management_account_rate_type_selections: Optional[
            "aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"
        ] = None,
        member_account_rate_type_selections: Optional[
            "aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"
        ] = None,
        standalone_account_rate_type_selections: Optional[
            "aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.update_preferences_response.UpdatePreferencesResponse":
        """<p> Updates the preferences for Pricing Calculator. </p>

        Args:
            management_account_rate_type_selections: <p> The updated preferred rate types for the management account. </p>
            member_account_rate_type_selections: <p> The updated preferred rate types for member accounts. </p>
            standalone_account_rate_type_selections: <p> The updated preferred rate types for a standalone account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.update_preferences_request.UpdatePreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.update_preferences_response.UpdatePreferencesResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_preferences

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_preferences.update_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_pricing_calculator.types.update_preferences_request.UpdatePreferencesRequest = {}  # type: ignore[typeddict-item]
        if management_account_rate_type_selections is not None:
            input_["management_account_rate_type_selections"] = (
                management_account_rate_type_selections
            )
        if member_account_rate_type_selections is not None:
            input_["member_account_rate_type_selections"] = (
                member_account_rate_type_selections
            )
        if standalone_account_rate_type_selections is not None:
            input_["standalone_account_rate_type_selections"] = (
                standalone_account_rate_type_selections
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
