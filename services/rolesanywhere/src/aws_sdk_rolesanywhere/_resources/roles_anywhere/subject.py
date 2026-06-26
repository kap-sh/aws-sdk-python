from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_rolesanywhere._auth._signers
import aws_sdk_rolesanywhere._auth._sigv4
from aws_sdk_rolesanywhere._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.list_request
    import aws_sdk_rolesanywhere.types.list_subjects_response
    import aws_sdk_rolesanywhere.types.scalar_subject_request
    import aws_sdk_rolesanywhere.types.subject_detail_response
    import aws_sdk_rolesanywhere.types.subject_summary
    import aws_sdk_rolesanywhere.types.uuid
    from aws_sdk_rolesanywhere._services.async_roles_anywhere import (
        AsyncRolesAnywhereClient,
        AsyncRolesAnywhereClientConfig,
    )
    from aws_sdk_rolesanywhere._services.roles_anywhere import (
        RolesAnywhereClient,
        RolesAnywhereClientConfig,
    )


class Subject:
    def __init__(self, service: RolesAnywhereClient) -> None:
        self._service = service

    def read(
        self,
        subject_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.subject_detail_response.SubjectDetailResponse":
        """<p>Gets a <i>subject</i>, which associates a certificate identity with authentication attempts. The subject stores auditing information such as the status of the last authentication attempt, the certificate data used in the attempt, and the last time the associated identity attempted authentication. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetSubject</code>. </p>

        Args:
            subject_id: <p>The unique identifier of the subject. </p>

        Raises:
            aws_sdk_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            aws_sdk_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.subject_detail_response.SubjectDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_subject

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.get_subject.get_subject(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest = {}  # type: ignore[typeddict-item]
        input_["subject_id"] = subject_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_subjects_response.ListSubjectsResponse":
        """<p>Lists the subjects in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListSubjects</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            aws_sdk_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            aws_sdk_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> OperationResponse[
            "aws_sdk_rolesanywhere.types.list_subjects_response.ListSubjectsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_subjects

            output, http_response = (
                aws_sdk_rolesanywhere._operations.roles_anywhere.list_subjects.list_subjects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.list_request.ListRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSubject:
    def __init__(self, service: AsyncRolesAnywhereClient) -> None:
        self._service = service

    async def read(
        self,
        subject_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.subject_detail_response.SubjectDetailResponse":
        """<p>Gets a <i>subject</i>, which associates a certificate identity with authentication attempts. The subject stores auditing information such as the status of the last authentication attempt, the certificate data used in the attempt, and the last time the associated identity attempted authentication. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetSubject</code>. </p>

        Args:
            subject_id: <p>The unique identifier of the subject. </p>

        Raises:
            aws_sdk_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            aws_sdk_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.subject_detail_response.SubjectDetailResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.get_subject

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.get_subject.async_get_subject(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest = {}  # type: ignore[typeddict-item]
        input_["subject_id"] = subject_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_subjects_response.ListSubjectsResponse":
        """<p>Lists the subjects in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListSubjects</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            aws_sdk_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            aws_sdk_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.list_subjects_response.ListSubjectsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_subjects

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.list_subjects.async_list_subjects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.list_request.ListRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
