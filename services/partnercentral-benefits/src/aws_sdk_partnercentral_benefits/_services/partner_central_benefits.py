"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#PartnerCentralBenefitsService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_partnercentral_benefits._auth._signers
import aws_sdk_partnercentral_benefits._auth._sigv4
from aws_sdk_partnercentral_benefits._auth._identity import Credentials
from aws_sdk_partnercentral_benefits._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_partnercentral_benefits._auth._zapros_handler import AuthMiddleware
from aws_sdk_partnercentral_benefits._pagination import resolve_path as _resolve_path
from aws_sdk_partnercentral_benefits._resources.partner_central_benefits_service.benefit import (
    Benefit,
)
from aws_sdk_partnercentral_benefits._resources.partner_central_benefits_service.benefit_allocation import (
    BenefitAllocation,
)
from aws_sdk_partnercentral_benefits._resources.partner_central_benefits_service.benefit_application import (
    BenefitApplication,
)
from aws_sdk_partnercentral_benefits._services._aws_config import aws_config
from aws_sdk_partnercentral_benefits._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.amend_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.amend_benefit_application_output
    import aws_sdk_partnercentral_benefits.types.amendment_list
    import aws_sdk_partnercentral_benefits.types.arn
    import aws_sdk_partnercentral_benefits.types.arns
    import aws_sdk_partnercentral_benefits.types.associate_benefit_application_resource_input
    import aws_sdk_partnercentral_benefits.types.associate_benefit_application_resource_output
    import aws_sdk_partnercentral_benefits.types.associated_resources
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_identifier
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_status_list
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_summary
    import aws_sdk_partnercentral_benefits.types.benefit_application_description
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier_list
    import aws_sdk_partnercentral_benefits.types.benefit_application_name
    import aws_sdk_partnercentral_benefits.types.benefit_application_summary
    import aws_sdk_partnercentral_benefits.types.benefit_identifiers
    import aws_sdk_partnercentral_benefits.types.benefit_statuses
    import aws_sdk_partnercentral_benefits.types.benefit_summary
    import aws_sdk_partnercentral_benefits.types.cancel_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.cancel_benefit_application_output
    import aws_sdk_partnercentral_benefits.types.catalog_name
    import aws_sdk_partnercentral_benefits.types.contacts
    import aws_sdk_partnercentral_benefits.types.create_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.create_benefit_application_output
    import aws_sdk_partnercentral_benefits.types.disassociate_benefit_application_resource_input
    import aws_sdk_partnercentral_benefits.types.disassociate_benefit_application_resource_output
    import aws_sdk_partnercentral_benefits.types.file_input_details
    import aws_sdk_partnercentral_benefits.types.fulfillment_types
    import aws_sdk_partnercentral_benefits.types.get_benefit_allocation_input
    import aws_sdk_partnercentral_benefits.types.get_benefit_allocation_output
    import aws_sdk_partnercentral_benefits.types.get_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.get_benefit_application_output
    import aws_sdk_partnercentral_benefits.types.get_benefit_input
    import aws_sdk_partnercentral_benefits.types.get_benefit_output
    import aws_sdk_partnercentral_benefits.types.list_benefit_allocations_input
    import aws_sdk_partnercentral_benefits.types.list_benefit_allocations_output
    import aws_sdk_partnercentral_benefits.types.list_benefit_applications_input
    import aws_sdk_partnercentral_benefits.types.list_benefit_applications_output
    import aws_sdk_partnercentral_benefits.types.list_benefits_input
    import aws_sdk_partnercentral_benefits.types.list_benefits_output
    import aws_sdk_partnercentral_benefits.types.list_tags_for_resource_request
    import aws_sdk_partnercentral_benefits.types.list_tags_for_resource_response
    import aws_sdk_partnercentral_benefits.types.programs
    import aws_sdk_partnercentral_benefits.types.recall_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.recall_benefit_application_output
    import aws_sdk_partnercentral_benefits.types.stages
    import aws_sdk_partnercentral_benefits.types.statuses
    import aws_sdk_partnercentral_benefits.types.submit_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.submit_benefit_application_output
    import aws_sdk_partnercentral_benefits.types.tag_key_list
    import aws_sdk_partnercentral_benefits.types.tag_resource_request
    import aws_sdk_partnercentral_benefits.types.tag_resource_response
    import aws_sdk_partnercentral_benefits.types.taggable_resource_arn
    import aws_sdk_partnercentral_benefits.types.tags
    import aws_sdk_partnercentral_benefits.types.untag_resource_request
    import aws_sdk_partnercentral_benefits.types.untag_resource_response
    import aws_sdk_partnercentral_benefits.types.update_benefit_application_input
    import aws_sdk_partnercentral_benefits.types.update_benefit_application_output


class PartnerCentralBenefitsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PartnerCentralBenefitsClient:
    """A client for the ``PartnerCentralBenefits`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = PartnerCentralBenefitsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.benefit = Benefit(self)
        self.benefit_allocation = BenefitAllocation(self)
        self.benefit_application = BenefitApplication(self)

    def operation_options(
        self, config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PartnerCentralBenefitsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def amend_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        client_token: str,
        revision: str,
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        amendment_reason: str,
        amendments: "aws_sdk_partnercentral_benefits.types.amendment_list.AmendmentList",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.amend_benefit_application_output.AmendBenefitApplicationOutput":
        """<p>Modifies an existing benefit application by applying amendments to specific fields while maintaining revision control.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the amendment request.</p>
            revision: <p>The current revision number of the benefit application to ensure optimistic concurrency control.</p>
            identifier: <p>The unique identifier of the benefit application to be amended.</p>
            amendment_reason: <p>A descriptive reason explaining why the benefit application is being amended.</p>
            amendments: <p>A list of specific field amendments to apply to the benefit application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.amend_benefit_application_input.AmendBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.amend_benefit_application_output.AmendBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.amend_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.amend_benefit_application.amend_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.amend_benefit_application_input.AmendBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["revision"] = revision
        input_["identifier"] = identifier
        input_["amendment_reason"] = amendment_reason
        input_["amendments"] = amendments

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_benefit_application_resource(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        benefit_application_identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        resource_arn: "aws_sdk_partnercentral_benefits.types.arn.Arn",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.associate_benefit_application_resource_output.AssociateBenefitApplicationResourceOutput":
        """<p>Links an AWS resource to an existing benefit application for tracking and management purposes.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            benefit_application_identifier: <p>The unique identifier of the benefit application to associate the resource with.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the AWS resource to associate with the benefit application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.associate_benefit_application_resource_input.AssociateBenefitApplicationResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.associate_benefit_application_resource_output.AssociateBenefitApplicationResourceOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.associate_benefit_application_resource

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.associate_benefit_application_resource.associate_benefit_application_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.associate_benefit_application_resource_input.AssociateBenefitApplicationResourceInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["benefit_application_identifier"] = benefit_application_identifier
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        client_token: str,
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        reason: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.cancel_benefit_application_output.CancelBenefitApplicationOutput":
        """<p>Cancels a benefit application that is currently in progress, preventing further processing.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the cancellation request.</p>
            identifier: <p>The unique identifier of the benefit application to cancel.</p>
            reason: <p>A descriptive reason explaining why the benefit application is being cancelled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.cancel_benefit_application_input.CancelBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.cancel_benefit_application_output.CancelBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.cancel_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.cancel_benefit_application.cancel_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.cancel_benefit_application_input.CancelBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        input_["identifier"] = identifier
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        client_token: str,
        benefit_identifier: str,
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        name: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
        ] = None,
        description: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_application_description.BenefitApplicationDescription"
        ] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        benefit_application_details: Optional[object] = None,
        tags: Optional["aws_sdk_partnercentral_benefits.types.tags.Tags"] = None,
        associated_resources: Optional[
            "aws_sdk_partnercentral_benefits.types.arns.Arns"
        ] = None,
        partner_contacts: Optional[
            "aws_sdk_partnercentral_benefits.types.contacts.Contacts"
        ] = None,
        file_details: Optional[
            "aws_sdk_partnercentral_benefits.types.file_input_details.FileInputDetails"
        ] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.create_benefit_application_output.CreateBenefitApplicationOutput":
        """<p>Creates a new benefit application for a partner to request access to AWS benefits and programs.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog to create the application in.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the creation request.</p>
            name: <p>A human-readable name for the benefit application.</p>
            description: <p>A detailed description of the benefit application and its intended use.</p>
            benefit_identifier: <p>The unique identifier of the benefit being requested in this application.</p>
            fulfillment_types: <p>The types of fulfillment requested for this benefit application (e.g., credits, access, disbursement).</p>
            benefit_application_details: <p>Detailed information and requirements specific to the benefit being requested.</p>
            tags: <p>Key-value pairs to categorize and organize the benefit application.</p>
            associated_resources: <p>AWS resources that are associated with this benefit application.</p>
            partner_contacts: <p>Contact information for partner representatives responsible for this benefit application.</p>
            file_details: <p>Supporting documents and files attached to the benefit application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.create_benefit_application_input.CreateBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.create_benefit_application_output.CreateBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.create_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.create_benefit_application.create_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.create_benefit_application_input.CreateBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["benefit_identifier"] = benefit_identifier
        if fulfillment_types is not None:
            input_["fulfillment_types"] = fulfillment_types
        if benefit_application_details is not None:
            input_["benefit_application_details"] = benefit_application_details
        if tags is not None:
            input_["tags"] = tags
        if associated_resources is not None:
            input_["associated_resources"] = associated_resources
        if partner_contacts is not None:
            input_["partner_contacts"] = partner_contacts
        if file_details is not None:
            input_["file_details"] = file_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_benefit_application_resource(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        benefit_application_identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        resource_arn: "aws_sdk_partnercentral_benefits.types.arn.Arn",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.disassociate_benefit_application_resource_output.DisassociateBenefitApplicationResourceOutput":
        """<p>Removes the association between an AWS resource and a benefit application.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            benefit_application_identifier: <p>The unique identifier of the benefit application to disassociate the resource from.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the AWS resource to disassociate from the benefit application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.disassociate_benefit_application_resource_input.DisassociateBenefitApplicationResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.disassociate_benefit_application_resource_output.DisassociateBenefitApplicationResourceOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.disassociate_benefit_application_resource

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.disassociate_benefit_application_resource.disassociate_benefit_application_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.disassociate_benefit_application_resource_input.DisassociateBenefitApplicationResourceInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["benefit_application_identifier"] = benefit_application_identifier
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_benefit(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        identifier: str,
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.get_benefit_output.GetBenefitOutput":
        """<p>Retrieves detailed information about a specific benefit available in the partner catalog.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog to query.</p>
            identifier: <p>The unique identifier of the benefit to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.get_benefit_input.GetBenefitInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.get_benefit_output.GetBenefitOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.get_benefit

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.get_benefit.get_benefit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.get_benefit_input.GetBenefitInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_benefit_allocation(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_allocation_identifier.BenefitAllocationIdentifier",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.get_benefit_allocation_output.GetBenefitAllocationOutput":
        """<p>Retrieves detailed information about a specific benefit allocation that has been granted to a partner.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog to query.</p>
            identifier: <p>The unique identifier of the benefit allocation to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.get_benefit_allocation_input.GetBenefitAllocationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.get_benefit_allocation_output.GetBenefitAllocationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.get_benefit_allocation

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.get_benefit_allocation.get_benefit_allocation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.get_benefit_allocation_input.GetBenefitAllocationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.get_benefit_application_output.GetBenefitApplicationOutput":
        """<p>Retrieves detailed information about a specific benefit application.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog to query.</p>
            identifier: <p>The unique identifier of the benefit application to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.get_benefit_application_input.GetBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.get_benefit_application_output.GetBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.get_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.get_benefit_application.get_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.get_benefit_application_input.GetBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_benefit_allocations(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        benefit_identifiers: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
        ] = None,
        benefit_application_identifiers: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_application_identifier_list.BenefitApplicationIdentifierList"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_allocation_status_list.BenefitAllocationStatusList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.list_benefit_allocations_output.ListBenefitAllocationsOutput":
        """<p>Retrieves a paginated list of benefit allocations based on specified filter criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter benefit allocations by catalog.</p>
            fulfillment_types: <p>Filter benefit allocations by specific fulfillment types.</p>
            benefit_identifiers: <p>Filter benefit allocations by specific benefit identifiers.</p>
            benefit_application_identifiers: <p>Filter benefit allocations by specific benefit application identifiers.</p>
            status: <p>Filter benefit allocations by their current status.</p>
            max_results: <p>The maximum number of benefit allocations to return in a single response.</p>
            next_token: <p>A pagination token to retrieve the next set of results from a previous request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.list_benefit_allocations_input.ListBenefitAllocationsInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.list_benefit_allocations_output.ListBenefitAllocationsOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_benefit_allocations

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_benefit_allocations.list_benefit_allocations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.list_benefit_allocations_input.ListBenefitAllocationsInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if fulfillment_types is not None:
            input_["fulfillment_types"] = fulfillment_types
        if benefit_identifiers is not None:
            input_["benefit_identifiers"] = benefit_identifiers
        if benefit_application_identifiers is not None:
            input_["benefit_application_identifiers"] = benefit_application_identifiers
        if status is not None:
            input_["status"] = status
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

    def iter_list_benefit_allocations(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        benefit_identifiers: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
        ] = None,
        benefit_application_identifiers: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_application_identifier_list.BenefitApplicationIdentifierList"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_allocation_status_list.BenefitAllocationStatusList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[aws_sdk_partnercentral_benefits.types.benefit_allocation_summary.BenefitAllocationSummary]":
        _token = next_token
        while True:
            _response = self.list_benefit_allocations(
                catalog,
                config_overrides=config_overrides,
                fulfillment_types=fulfillment_types,
                benefit_identifiers=benefit_identifiers,
                benefit_application_identifiers=benefit_application_identifiers,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("benefit_allocation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_benefit_applications(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        programs: Optional[
            "aws_sdk_partnercentral_benefits.types.programs.Programs"
        ] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        benefit_identifiers: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_benefits.types.statuses.Statuses"
        ] = None,
        stages: Optional["aws_sdk_partnercentral_benefits.types.stages.Stages"] = None,
        associated_resources: Optional[
            "aws_sdk_partnercentral_benefits.types.associated_resources.AssociatedResources"
        ] = None,
        associated_resource_arns: Optional[
            "aws_sdk_partnercentral_benefits.types.arns.Arns"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.list_benefit_applications_output.ListBenefitApplicationsOutput":
        """<p>Retrieves a paginated list of benefit applications based on specified filter criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter benefit applications by catalog.</p>
            programs: <p>Filter benefit applications by specific AWS partner programs.</p>
            fulfillment_types: <p>Filter benefit applications by specific fulfillment types.</p>
            benefit_identifiers: <p>Filter benefit applications by specific benefit identifiers.</p>
            status: <p>Filter benefit applications by their current processing status.</p>
            stages: <p>Filter benefit applications by their current processing stage.</p>
            associated_resources: <p>Filter benefit applications by associated AWS resources.</p>
            associated_resource_arns: <p>Filter benefit applications by specific AWS resource ARNs.</p>
            max_results: <p>The maximum number of benefit applications to return in a single response.</p>
            next_token: <p>A pagination token to retrieve the next set of results from a previous request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.list_benefit_applications_input.ListBenefitApplicationsInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.list_benefit_applications_output.ListBenefitApplicationsOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_benefit_applications

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_benefit_applications.list_benefit_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.list_benefit_applications_input.ListBenefitApplicationsInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if programs is not None:
            input_["programs"] = programs
        if fulfillment_types is not None:
            input_["fulfillment_types"] = fulfillment_types
        if benefit_identifiers is not None:
            input_["benefit_identifiers"] = benefit_identifiers
        if status is not None:
            input_["status"] = status
        if stages is not None:
            input_["stages"] = stages
        if associated_resources is not None:
            input_["associated_resources"] = associated_resources
        if associated_resource_arns is not None:
            input_["associated_resource_arns"] = associated_resource_arns
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

    def iter_list_benefit_applications(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        programs: Optional[
            "aws_sdk_partnercentral_benefits.types.programs.Programs"
        ] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        benefit_identifiers: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_identifiers.BenefitIdentifiers"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_benefits.types.statuses.Statuses"
        ] = None,
        stages: Optional["aws_sdk_partnercentral_benefits.types.stages.Stages"] = None,
        associated_resources: Optional[
            "aws_sdk_partnercentral_benefits.types.associated_resources.AssociatedResources"
        ] = None,
        associated_resource_arns: Optional[
            "aws_sdk_partnercentral_benefits.types.arns.Arns"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[aws_sdk_partnercentral_benefits.types.benefit_application_summary.BenefitApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_benefit_applications(
                catalog,
                config_overrides=config_overrides,
                programs=programs,
                fulfillment_types=fulfillment_types,
                benefit_identifiers=benefit_identifiers,
                status=status,
                stages=stages,
                associated_resources=associated_resources,
                associated_resource_arns=associated_resource_arns,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("benefit_application_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_benefits(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        programs: Optional[
            "aws_sdk_partnercentral_benefits.types.programs.Programs"
        ] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_statuses.BenefitStatuses"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "aws_sdk_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput"
    ):
        """<p>Retrieves a paginated list of available benefits based on specified filter criteria.</p>

        Args:
            catalog: <p>The catalog identifier to filter benefits by catalog.</p>
            programs: <p>Filter benefits by specific AWS partner programs.</p>
            fulfillment_types: <p>Filter benefits by specific fulfillment types.</p>
            status: <p>Filter benefits by their current status.</p>
            max_results: <p>The maximum number of benefits to return in a single response.</p>
            next_token: <p>A pagination token to retrieve the next set of results from a previous request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.list_benefits_input.ListBenefitsInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.list_benefits_output.ListBenefitsOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_benefits

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_benefits.list_benefits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.list_benefits_input.ListBenefitsInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if programs is not None:
            input_["programs"] = programs
        if fulfillment_types is not None:
            input_["fulfillment_types"] = fulfillment_types
        if status is not None:
            input_["status"] = status
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

    def iter_list_benefits(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        programs: Optional[
            "aws_sdk_partnercentral_benefits.types.programs.Programs"
        ] = None,
        fulfillment_types: Optional[
            "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_statuses.BenefitStatuses"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "Iterator[aws_sdk_partnercentral_benefits.types.benefit_summary.BenefitSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_benefits(
                catalog,
                config_overrides=config_overrides,
                programs=programs,
                fulfillment_types=fulfillment_types,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("benefit_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_benefits.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves all tags associated with a specific resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def recall_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        reason: str,
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.recall_benefit_application_output.RecallBenefitApplicationOutput":
        """<p>Recalls a submitted benefit application, returning it to draft status for further modifications.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the recall request.</p>
            identifier: <p>The unique identifier of the benefit application to recall.</p>
            reason: <p>A descriptive reason explaining why the benefit application is being recalled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.recall_benefit_application_input.RecallBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.recall_benefit_application_output.RecallBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.recall_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.recall_benefit_application.recall_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.recall_benefit_application_input.RecallBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if client_token is not None:
            input_["client_token"] = client_token
        input_["identifier"] = identifier
        input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def submit_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.submit_benefit_application_output.SubmitBenefitApplicationOutput":
        """<p>Submits a benefit application for review and processing by AWS.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            identifier: <p>The unique identifier of the benefit application to submit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.submit_benefit_application_input.SubmitBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.submit_benefit_application_output.SubmitBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.submit_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.submit_benefit_application.submit_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.submit_benefit_application_input.SubmitBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_benefits.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_partnercentral_benefits.types.tags.Tags",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>A list of key-value pairs to add as tags to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.tag_resource

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_benefits.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_partnercentral_benefits.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.untag_resource

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_benefit_application(
        self,
        catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName",
        client_token: str,
        identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier",
        revision: str,
        *,
        config_overrides: Optional[PartnerCentralBenefitsClientConfig] = None,
        name: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
        ] = None,
        description: Optional[
            "aws_sdk_partnercentral_benefits.types.benefit_application_description.BenefitApplicationDescription"
        ] = None,
        benefit_application_details: Optional[object] = None,
        partner_contacts: Optional[
            "aws_sdk_partnercentral_benefits.types.contacts.Contacts"
        ] = None,
        file_details: Optional[
            "aws_sdk_partnercentral_benefits.types.file_input_details.FileInputDetails"
        ] = None,
    ) -> "aws_sdk_partnercentral_benefits.types.update_benefit_application_output.UpdateBenefitApplicationOutput":
        """<p>Updates an existing benefit application with new information while maintaining revision control.</p>

        Args:
            catalog: <p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the update request.</p>
            name: <p>The updated human-readable name for the benefit application.</p>
            description: <p>The updated detailed description of the benefit application.</p>
            identifier: <p>The unique identifier of the benefit application to update.</p>
            revision: <p>The current revision number of the benefit application to ensure optimistic concurrency control.</p>
            benefit_application_details: <p>Updated detailed information and requirements specific to the benefit being requested.</p>
            partner_contacts: <p>Updated contact information for partner representatives responsible for this benefit application.</p>
            file_details: <p>Updated supporting documents and files attached to the benefit application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_benefits.types.update_benefit_application_input.UpdateBenefitApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_benefits.types.update_benefit_application_output.UpdateBenefitApplicationOutput"
        ]:
            import aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.update_benefit_application

            output, http_response = (
                aws_sdk_partnercentral_benefits._operations.partner_central_benefits_service.update_benefit_application.update_benefit_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_benefits.types.update_benefit_application_input.UpdateBenefitApplicationInput = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["identifier"] = identifier
        input_["revision"] = revision
        if benefit_application_details is not None:
            input_["benefit_application_details"] = benefit_application_details
        if partner_contacts is not None:
            input_["partner_contacts"] = partner_contacts
        if file_details is not None:
            input_["file_details"] = file_details

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
