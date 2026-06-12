from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_account._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.alliance_lead_contact
    import aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_request
    import aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_response
    import aws_sdk_partnercentral_account.types.cancel_profile_update_task_request
    import aws_sdk_partnercentral_account.types.cancel_profile_update_task_response
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.create_partner_request
    import aws_sdk_partnercentral_account.types.create_partner_response
    import aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request
    import aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response
    import aws_sdk_partnercentral_account.types.domain_name
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.email_verification_code
    import aws_sdk_partnercentral_account.types.get_alliance_lead_contact_request
    import aws_sdk_partnercentral_account.types.get_alliance_lead_contact_response
    import aws_sdk_partnercentral_account.types.get_partner_request
    import aws_sdk_partnercentral_account.types.get_partner_response
    import aws_sdk_partnercentral_account.types.get_profile_update_task_request
    import aws_sdk_partnercentral_account.types.get_profile_update_task_response
    import aws_sdk_partnercentral_account.types.get_profile_visibility_request
    import aws_sdk_partnercentral_account.types.get_profile_visibility_response
    import aws_sdk_partnercentral_account.types.list_partners_request
    import aws_sdk_partnercentral_account.types.list_partners_response
    import aws_sdk_partnercentral_account.types.next_token
    import aws_sdk_partnercentral_account.types.partner_identifier
    import aws_sdk_partnercentral_account.types.partner_summary
    import aws_sdk_partnercentral_account.types.primary_solution_type
    import aws_sdk_partnercentral_account.types.profile_task_id
    import aws_sdk_partnercentral_account.types.profile_visibility
    import aws_sdk_partnercentral_account.types.put_alliance_lead_contact_request
    import aws_sdk_partnercentral_account.types.put_alliance_lead_contact_response
    import aws_sdk_partnercentral_account.types.put_profile_visibility_request
    import aws_sdk_partnercentral_account.types.put_profile_visibility_response
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string
    import aws_sdk_partnercentral_account.types.start_profile_update_task_request
    import aws_sdk_partnercentral_account.types.start_profile_update_task_response
    import aws_sdk_partnercentral_account.types.tag_list
    import aws_sdk_partnercentral_account.types.task_details
    from aws_sdk_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from aws_sdk_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class Partner:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        legal_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        primary_solution_type: "aws_sdk_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
        alliance_lead_contact: "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        email_verification_code: "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_partnercentral_account.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_account.types.create_partner_response.CreatePartnerResponse":
        """<p>Creates a new partner account in the AWS Partner Network with the specified details and configuration.</p>

        Args:
            catalog: <p>The catalog identifier where the partner account will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            legal_name: <p>The legal name of the organization becoming a partner.</p>
            primary_solution_type: <p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>
            alliance_lead_contact: <p>The primary contact person for alliance and partnership matters.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>
            tags: <p>A list of tags to associate with the partner account for organization and billing purposes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.create_partner_request.CreatePartnerRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.create_partner_response.CreatePartnerResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.create_partner

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.create_partner.create_partner(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.create_partner_request.CreatePartnerRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if client_token is not None:
            input["client_token"] = client_token
        input["legal_name"] = legal_name
        input["primary_solution_type"] = primary_solution_type
        input["alliance_lead_contact"] = alliance_lead_contact
        input["email_verification_code"] = email_verification_code
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_partner_response.GetPartnerResponse":
        """<p>Retrieves detailed information about a specific partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_partner_request.GetPartnerRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_partner_response.GetPartnerResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_partner

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_partner.get_partner(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_partner_request.GetPartnerRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_account.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_partners_response.ListPartnersResponse":
        """<p>Lists partner accounts in the catalog, providing a summary view of all partners.</p>

        Args:
            catalog: <p>The catalog identifier to list partners from.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.list_partners_request.ListPartnersRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.list_partners_response.ListPartnersResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_partners

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.list_partners.list_partners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.list_partners_request.ListPartnersRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_aws_training_certification_email_domain(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        email: "aws_sdk_partnercentral_account.types.email.Email",
        email_verification_code: "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Associates an email domain with AWS training and certification for the partner account, enabling automatic verification of employee certifications.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            email: <p>The email address used to verify domain ownership for AWS training and certification association.</p>
            email_verification_code: <p>The verification code sent to the email address to confirm domain ownership.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain.associate_aws_training_certification_email_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["email"] = email
        input["email_verification_code"] = email_verification_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_profile_update_task(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_id: "aws_sdk_partnercentral_account.types.profile_task_id.ProfileTaskId",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse":
        """<p>Cancels an in-progress profile update task, stopping any pending changes to the partner profile.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_id: <p>The unique identifier of the profile update task to cancel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.cancel_profile_update_task

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.cancel_profile_update_task.cancel_profile_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_aws_training_certification_email_domain(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        domain_name: "aws_sdk_partnercentral_account.types.domain_name.DomainName",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Removes the association between an email domain and AWS training and certification for the partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            domain_name: <p>The domain name to disassociate from AWS training and certification.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain.disassociate_aws_training_certification_email_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_alliance_lead_contact(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse":
        """<p>Retrieves the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact.get_alliance_lead_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_profile_update_task(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse":
        """<p>Retrieves information about a specific profile update task.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_update_task

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_update_task.get_profile_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_profile_visibility(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse":
        """<p>Retrieves the visibility settings for a partner profile, determining who can see the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_visibility

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_visibility.get_profile_visibility(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_alliance_lead_contact(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        alliance_lead_contact: "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        email_verification_code: Optional[
            "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse":
        """<p>Creates or updates the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            alliance_lead_contact: <p>The alliance lead contact information to set for the partner account.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm the update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact.put_alliance_lead_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        input["alliance_lead_contact"] = alliance_lead_contact
        if email_verification_code is not None:
            input["email_verification_code"] = email_verification_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_profile_visibility(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        visibility: "aws_sdk_partnercentral_account.types.profile_visibility.ProfileVisibility",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse":
        """<p>Sets the visibility level for a partner profile, controlling who can view the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            visibility: <p>The visibility setting to apply to the partner profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.put_profile_visibility

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.put_profile_visibility.put_profile_visibility(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        input["visibility"] = visibility

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_profile_update_task(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_details: "aws_sdk_partnercentral_account.types.task_details.TaskDetails",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse":
        """<p>Initiates a profile update task to modify partner profile information asynchronously.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_details: <p>The details of the profile updates to be performed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.start_profile_update_task

            output, http_response = (
                aws_sdk_partnercentral_account._operations.partner_central_account.start_profile_update_task.start_profile_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["task_details"] = task_details

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPartner:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        legal_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        primary_solution_type: "aws_sdk_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
        alliance_lead_contact: "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        email_verification_code: "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_partnercentral_account.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_account.types.create_partner_response.CreatePartnerResponse":
        """<p>Creates a new partner account in the AWS Partner Network with the specified details and configuration.</p>

        Args:
            catalog: <p>The catalog identifier where the partner account will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            legal_name: <p>The legal name of the organization becoming a partner.</p>
            primary_solution_type: <p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>
            alliance_lead_contact: <p>The primary contact person for alliance and partnership matters.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>
            tags: <p>A list of tags to associate with the partner account for organization and billing purposes.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.create_partner_request.CreatePartnerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.create_partner_response.CreatePartnerResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.create_partner

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.create_partner.async_create_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.create_partner_request.CreatePartnerRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if client_token is not None:
            input["client_token"] = client_token
        input["legal_name"] = legal_name
        input["primary_solution_type"] = primary_solution_type
        input["alliance_lead_contact"] = alliance_lead_contact
        input["email_verification_code"] = email_verification_code
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_partner_response.GetPartnerResponse":
        """<p>Retrieves detailed information about a specific partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_partner_request.GetPartnerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_partner_response.GetPartnerResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_partner

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_partner.async_get_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_partner_request.GetPartnerRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "aws_sdk_partnercentral_account.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_partners_response.ListPartnersResponse":
        """<p>Lists partner accounts in the catalog, providing a summary view of all partners.</p>

        Args:
            catalog: <p>The catalog identifier to list partners from.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.list_partners_request.ListPartnersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.list_partners_response.ListPartnersResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_partners

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.list_partners.async_list_partners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.list_partners_request.ListPartnersRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_aws_training_certification_email_domain(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        email: "aws_sdk_partnercentral_account.types.email.Email",
        email_verification_code: "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Associates an email domain with AWS training and certification for the partner account, enabling automatic verification of employee certifications.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            email: <p>The email address used to verify domain ownership for AWS training and certification association.</p>
            email_verification_code: <p>The verification code sent to the email address to confirm domain ownership.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain.async_associate_aws_training_certification_email_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["email"] = email
        input["email_verification_code"] = email_verification_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_profile_update_task(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_id: "aws_sdk_partnercentral_account.types.profile_task_id.ProfileTaskId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse":
        """<p>Cancels an in-progress profile update task, stopping any pending changes to the partner profile.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_id: <p>The unique identifier of the profile update task to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.cancel_profile_update_task

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.cancel_profile_update_task.async_cancel_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_aws_training_certification_email_domain(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        domain_name: "aws_sdk_partnercentral_account.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Removes the association between an email domain and AWS training and certification for the partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            domain_name: <p>The domain name to disassociate from AWS training and certification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain.async_disassociate_aws_training_certification_email_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_alliance_lead_contact(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse":
        """<p>Retrieves the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact.async_get_alliance_lead_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_profile_update_task(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse":
        """<p>Retrieves information about a specific profile update task.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_update_task

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_update_task.async_get_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_profile_visibility(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse":
        """<p>Retrieves the visibility settings for a partner profile, determining who can see the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_visibility

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_profile_visibility.async_get_profile_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_alliance_lead_contact(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        alliance_lead_contact: "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        email_verification_code: Optional[
            "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse":
        """<p>Creates or updates the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            alliance_lead_contact: <p>The alliance lead contact information to set for the partner account.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm the update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact.async_put_alliance_lead_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        input["alliance_lead_contact"] = alliance_lead_contact
        if email_verification_code is not None:
            input["email_verification_code"] = email_verification_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_profile_visibility(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        visibility: "aws_sdk_partnercentral_account.types.profile_visibility.ProfileVisibility",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse":
        """<p>Sets the visibility level for a partner profile, controlling who can view the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            visibility: <p>The visibility setting to apply to the partner profile.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.put_profile_visibility

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.put_profile_visibility.async_put_profile_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        input["visibility"] = visibility

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_profile_update_task(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        identifier: "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_details: "aws_sdk_partnercentral_account.types.task_details.TaskDetails",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse":
        """<p>Initiates a profile update task to modify partner profile information asynchronously.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_details: <p>The details of the profile updates to be performed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.start_profile_update_task

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.start_profile_update_task.async_start_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["identifier"] = identifier
        if client_token is not None:
            input["client_token"] = client_token
        input["task_details"] = task_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
