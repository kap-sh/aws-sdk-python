"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#AWSMPMeteringService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_marketplace_metering._auth._identity import Credentials
from aws_sdk_marketplace_metering._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_marketplace_metering._auth._zapros_handler import AuthMiddleware
from aws_sdk_marketplace_metering._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.batch_meter_usage_request
    import aws_sdk_marketplace_metering.types.batch_meter_usage_result
    import aws_sdk_marketplace_metering.types.boolean
    import aws_sdk_marketplace_metering.types.client_token
    import aws_sdk_marketplace_metering.types.meter_usage_request
    import aws_sdk_marketplace_metering.types.meter_usage_result
    import aws_sdk_marketplace_metering.types.non_empty_string
    import aws_sdk_marketplace_metering.types.nonce
    import aws_sdk_marketplace_metering.types.product_code
    import aws_sdk_marketplace_metering.types.register_usage_request
    import aws_sdk_marketplace_metering.types.register_usage_result
    import aws_sdk_marketplace_metering.types.resolve_customer_request
    import aws_sdk_marketplace_metering.types.resolve_customer_result
    import aws_sdk_marketplace_metering.types.timestamp
    import aws_sdk_marketplace_metering.types.usage_allocations
    import aws_sdk_marketplace_metering.types.usage_dimension
    import aws_sdk_marketplace_metering.types.usage_quantity
    import aws_sdk_marketplace_metering.types.usage_record_list
    import aws_sdk_marketplace_metering.types.version_integer


class MarketplaceMeteringClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
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


class MarketplaceMeteringClient:
    """A client for the ``MarketplaceMetering`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
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
        use_dual_stack: bool | None = None,
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
        self.config = MarketplaceMeteringClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MarketplaceMeteringClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MarketplaceMeteringClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_meter_usage(
        self,
        usage_records: "aws_sdk_marketplace_metering.types.usage_record_list.UsageRecordList",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
        product_code: Optional[
            "aws_sdk_marketplace_metering.types.product_code.ProductCode"
        ] = None,
    ) -> "aws_sdk_marketplace_metering.types.batch_meter_usage_result.BatchMeterUsageResult":
        """<important> <p>Amazon Web Services Marketplace is introducing Concurrent Agreements, enabling buyers to make multiple purchases per Amazon Web Services account. Starting June 1, 2026, new SaaS products must use <code>CustomerAWSAccountId</code> (instead of <code>CustomerIdentifier</code>), <code>LicenseArn</code> (instead of <code>ProductCode</code>) to support this feature. Existing integrations will continue to work. Review the new integration for Concurrent Agreements <a href=\"https://catalog.workshops.aws/mpseller/en-US/saas/integration-for-concurrent-agreements\">here</a>.</p> </important> <p>To post metering records for customers, SaaS applications call <code>BatchMeterUsage</code>, which is used for metering SaaS flexible consumption pricing (FCP). Identical requests are idempotent and can be retried with the same records or a subset of records. Each <code>BatchMeterUsage</code> request is for only one product. If you want to meter usage for multiple products, you must make multiple <code>BatchMeterUsage</code> calls.</p> <p>Usage records should be submitted in quick succession following a recorded event. Usage records aren't accepted 6 hours or more after an event.</p> <p> <code>BatchMeterUsage</code> can process up to 25 <code>UsageRecords</code> at a time, and each request must be less than 1 MB in size. Optionally, you can have multiple usage allocations for usage data that's split into buckets according to predefined tags.</p> <p> <code>BatchMeterUsage</code> returns a list of <code>UsageRecordResult</code> objects, which have each <code>UsageRecord</code>. It also returns a list of <code>UnprocessedRecords</code>, which indicate errors on the service side that should be retried.</p> <p>For Amazon Web Services Regions that support <code>BatchMeterUsage</code>, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#batchmeterusage-region-support\">BatchMeterUsage Region support</a>. </p> <note> <p>For an example of <code>BatchMeterUsage</code>, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-example\"> BatchMeterUsage code example</a> in the <i>Amazon Web Services Marketplace Seller Guide</i>.</p> </note>

        Args:
            usage_records: <p>The set of <code>UsageRecords</code> to submit. <code>BatchMeterUsage</code> accepts up to 25 <code>UsageRecords</code> at a time.</p>
            product_code: <p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_metering.types.batch_meter_usage_request.BatchMeterUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_metering.types.batch_meter_usage_result.BatchMeterUsageResult"
        ]:
            import aws_sdk_marketplace_metering._operations.awsmp_metering_service.batch_meter_usage

            output, http_response = (
                aws_sdk_marketplace_metering._operations.awsmp_metering_service.batch_meter_usage.batch_meter_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_metering.types.batch_meter_usage_request.BatchMeterUsageRequest = {}  # type: ignore[typeddict-item]
        input["usage_records"] = usage_records
        if product_code is not None:
            input["product_code"] = product_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def meter_usage(
        self,
        product_code: "aws_sdk_marketplace_metering.types.product_code.ProductCode",
        timestamp: "aws_sdk_marketplace_metering.types.timestamp.Timestamp",
        usage_dimension: "aws_sdk_marketplace_metering.types.usage_dimension.UsageDimension",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
        usage_quantity: Optional[
            "aws_sdk_marketplace_metering.types.usage_quantity.UsageQuantity"
        ] = None,
        dry_run: Optional["aws_sdk_marketplace_metering.types.boolean.Boolean"] = None,
        usage_allocations: Optional[
            "aws_sdk_marketplace_metering.types.usage_allocations.UsageAllocations"
        ] = None,
        client_token: Optional[
            "aws_sdk_marketplace_metering.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_marketplace_metering.types.meter_usage_result.MeterUsageResult":
        """<p>As a seller, your software hosted in the buyer's Amazon Web Services account uses this API action to emit metering records directly to Amazon Web Services Marketplace. You must use the following buyer Amazon Web Services account credentials to sign the API request.</p> <ul> <li> <p>For <b>Amazon EC2</b> deployments, your software must use the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html\">IAM role for Amazon EC2</a> to sign the API call for <code>MeterUsage</code> API operation.</p> </li> <li> <p>For <b>Amazon EKS</b> deployments, your software must use <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html\">IAM roles for service accounts (IRSA)</a> to sign the API call for the <code>MeterUsage</code> API operation. Using <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html\">EKS Pod Identity</a>, the node role, or long-term access keys is not supported.</p> </li> <li> <p>For <b>Amazon ECS</b> deployments, your software must use <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html\">Amazon ECS task IAM</a> role to sign the API call for the <code>MeterUsage</code> API operation. Using the node role or long-term access keys are not supported.</p> </li> <li> <p>For <b>Amazon Bedrock AgentCore Runtime</b> deployments, your software must use the <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#runtime-permissions-execution\">AgentCore Runtime execution role</a> to sign the API call for the <code>MeterUsage</code> API operation. Long-term access keys are not supported.</p> </li> </ul> <p>The handling of <code>MeterUsage</code> requests varies between Amazon Bedrock AgentCore Runtime and non-Amazon Bedrock AgentCore deployments.</p> <ul> <li> <p>For <b>non-Amazon Bedrock AgentCore Runtime</b> deployments, you can only report usage once per hour for each dimension. For AMI-based products, this is per dimension and per EC2 instance. For container products, this is per dimension and per ECS task or EKS pod. You can't modify values after they're recorded. If you report usage before a current hour ends, you will be unable to report additional usage until the next hour begins. The <code>Timestamp</code> request parameter is rounded down to the hour and used to enforce this once-per-hour rule for idempotency. For requests that are identical after the <code>Timestamp</code> is rounded down, the API is idempotent and returns the metering record ID.</p> </li> <li> <p>For <b>Amazon Bedrock AgentCore Runtime</b> deployments, you can report usage multiple times per hour for the same dimension. You do not need to aggregate metering records by the hour. You must include an idempotency token in the <code>ClientToken</code> request parameter. If using an Amazon SDK or the Amazon Web Services CLI, you must use the latest version which automatically includes an idempotency token in the <code>ClientToken</code> request parameter so that the request is processed successfully. The <code>Timestamp</code> request parameter is not rounded down to the hour and is not used for duplicate validation. Requests with duplicate <code>Timestamps</code> are aggregated as long as the <code>ClientToken</code> is unique.</p> </li> </ul> <p>If you submit records more than six hours after events occur, the records won't be accepted. The timestamp in your request determines when an event is recorded.</p> <p>You can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define or allow the customer to define.</p> <p>For Amazon Web Services Regions that support <code>MeterUsage</code>, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ec2\">MeterUsage Region support for Amazon EC2</a> and <a href=\"https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ecs-eks\">MeterUsage Region support for Amazon ECS and Amazon EKS</a>. </p>

        Args:
            product_code: <p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>
            timestamp: <p>Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to six hours in the past. Make sure the <code>timestamp</code> value is not before the start of the software usage.</p>
            usage_dimension: <p>It will be one of the fcp dimension name provided during the publishing of the product.</p>
            usage_quantity: <p>Consumption value for the hour. Defaults to <code>0</code> if not specified.</p>
            dry_run: <p>Checks whether you have the permissions required for the action, but does not make the request. If you have the permissions, the request returns <code>DryRunOperation</code>; otherwise, it returns <code>UnauthorizedException</code>. Defaults to <code>false</code> if not specified.</p>
            usage_allocations: <p>The set of <code>UsageAllocations</code> to submit.</p> <p>The sum of all <code>UsageAllocation</code> quantities must equal the <code>UsageQuantity</code> of the <code>MeterUsage</code> request, and each <code>UsageAllocation</code> must have a unique set of tags (include no tags).</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotencyConflictException</code> error.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_metering.types.meter_usage_request.MeterUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_metering.types.meter_usage_result.MeterUsageResult"
        ]:
            import aws_sdk_marketplace_metering._operations.awsmp_metering_service.meter_usage

            output, http_response = (
                aws_sdk_marketplace_metering._operations.awsmp_metering_service.meter_usage.meter_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_metering.types.meter_usage_request.MeterUsageRequest = {}  # type: ignore[typeddict-item]
        input["product_code"] = product_code
        input["timestamp"] = timestamp
        input["usage_dimension"] = usage_dimension
        if usage_quantity is not None:
            input["usage_quantity"] = usage_quantity
        if dry_run is not None:
            input["dry_run"] = dry_run
        if usage_allocations is not None:
            input["usage_allocations"] = usage_allocations
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_usage(
        self,
        product_code: "aws_sdk_marketplace_metering.types.product_code.ProductCode",
        public_key_version: "aws_sdk_marketplace_metering.types.version_integer.VersionInteger",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
        nonce: Optional["aws_sdk_marketplace_metering.types.nonce.Nonce"] = None,
    ) -> "aws_sdk_marketplace_metering.types.register_usage_result.RegisterUsageResult":
        """<p>Paid container software products sold through Amazon Web Services Marketplace must integrate with the Amazon Web Services Marketplace Metering Service and call the <code>RegisterUsage</code> operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren't required to call <code>RegisterUsage</code>, but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of <code>RegisterUsage</code>. <code>RegisterUsage</code> performs two primary functions: metering and entitlement.</p> <ul> <li> <p> <i>Entitlement</i>: <code>RegisterUsage</code> allows you to verify that the customer running your paid software is subscribed to your product on Amazon Web Services Marketplace, enabling you to guard against unauthorized use. Your container image that integrates with <code>RegisterUsage</code> is only required to guard against unauthorized use at container startup, as such a <code>CustomerNotSubscribedException</code> or <code>PlatformNotSupportedException</code> will only be thrown on the initial call to <code>RegisterUsage</code>. Subsequent calls from the same Amazon ECS task instance (e.g. task-id) or Amazon EKS pod will not throw a <code>CustomerNotSubscribedException</code>, even if the customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.</p> </li> <li> <p> <i>Metering</i>: <code>RegisterUsage</code> meters software use per ECS task, per hour, or per pod for Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will launch a task on all 10 cluster nodes and the customer will be charged for 10 tasks. Software metering is handled by the Amazon Web Services Marketplace metering control plane—your software is not required to perform metering-specific actions other than to call <code>RegisterUsage</code> to commence metering. The Amazon Web Services Marketplace metering control plane will also bill customers for running ECS tasks and Amazon EKS pods, regardless of the customer's subscription state, which removes the need for your software to run entitlement checks at runtime. For containers, <code>RegisterUsage</code> should be called immediately at launch. If you don’t register the container within the first 6 hours of the launch, Amazon Web Services Marketplace Metering Service doesn’t provide any metering guarantees for previous months. Metering will continue, however, for the current month forward until the container ends. <code>RegisterUsage</code> is for metering paid hourly container products.</p> <p>For Amazon Web Services Regions that support <code>RegisterUsage</code>, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#registerusage-region-support\">RegisterUsage Region support</a>. </p> </li> </ul>

        Args:
            product_code: <p>Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.</p>
            public_key_version: <p>Public Key Version provided by Amazon Web Services Marketplace</p>
            nonce: <p>(Optional) To scope down the registration to a specific running software instance and guard against replay attacks.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_metering.types.register_usage_request.RegisterUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_metering.types.register_usage_result.RegisterUsageResult"
        ]:
            import aws_sdk_marketplace_metering._operations.awsmp_metering_service.register_usage

            output, http_response = (
                aws_sdk_marketplace_metering._operations.awsmp_metering_service.register_usage.register_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_metering.types.register_usage_request.RegisterUsageRequest = {}  # type: ignore[typeddict-item]
        input["product_code"] = product_code
        input["public_key_version"] = public_key_version
        if nonce is not None:
            input["nonce"] = nonce

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def resolve_customer(
        self,
        registration_token: "aws_sdk_marketplace_metering.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[MarketplaceMeteringClientConfig] = None,
    ) -> "aws_sdk_marketplace_metering.types.resolve_customer_result.ResolveCustomerResult":
        """<p> <code>ResolveCustomer</code> is called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a registration token through their browser. The registration token is resolved through this API to obtain a <code>CustomerIdentifier</code> along with the <code>CustomerAWSAccountId</code>, <code>ProductCode</code>, and <code>LicenseArn</code>.</p> <note> <p>To successfully resolve the token, the API must be called from the account that was used to publish the SaaS application. For an example of using <code>ResolveCustomer</code>, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-resolvecustomer-example\"> ResolveCustomer code example</a> in the <i>Amazon Web Services Marketplace Seller Guide</i>.</p> </note> <p>Permission is required for this operation. Your IAM role or user performing this operation requires a policy to allow the <code>aws-marketplace:ResolveCustomer</code> action. For more information, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsmarketplacemeteringservice.html\">Actions, resources, and condition keys for Amazon Web Services Marketplace Metering Service</a> in the <i>Service Authorization Reference</i>.</p> <p>For Amazon Web Services Regions that support <code>ResolveCustomer</code>, see <a href=\"https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#resolvecustomer-region-support\">ResolveCustomer Region support</a>. </p>

        Args:
            registration_token: <p>When a buyer visits your website during the registration process, the buyer submits a registration token through the browser. The registration token is resolved to obtain a <code>CustomerIdentifier</code> along with the <code>CustomerAWSAccountId</code>, <code>ProductCode</code>, and <code>LicenseArn</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_metering.types.resolve_customer_request.ResolveCustomerRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_metering.types.resolve_customer_result.ResolveCustomerResult"
        ]:
            import aws_sdk_marketplace_metering._operations.awsmp_metering_service.resolve_customer

            output, http_response = (
                aws_sdk_marketplace_metering._operations.awsmp_metering_service.resolve_customer.resolve_customer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_metering.types.resolve_customer_request.ResolveCustomerRequest = {}  # type: ignore[typeddict-item]
        input["registration_token"] = registration_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
