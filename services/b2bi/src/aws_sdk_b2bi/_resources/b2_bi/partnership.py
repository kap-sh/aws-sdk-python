from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_b2bi._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_options
    import aws_sdk_b2bi.types.create_partnership_request
    import aws_sdk_b2bi.types.create_partnership_response
    import aws_sdk_b2bi.types.delete_partnership_request
    import aws_sdk_b2bi.types.email
    import aws_sdk_b2bi.types.get_partnership_request
    import aws_sdk_b2bi.types.get_partnership_response
    import aws_sdk_b2bi.types.list_partnerships_request
    import aws_sdk_b2bi.types.list_partnerships_response
    import aws_sdk_b2bi.types.max_results
    import aws_sdk_b2bi.types.page_token
    import aws_sdk_b2bi.types.partner_name
    import aws_sdk_b2bi.types.partnership_capabilities
    import aws_sdk_b2bi.types.partnership_id
    import aws_sdk_b2bi.types.partnership_summary
    import aws_sdk_b2bi.types.phone
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.tag_list
    import aws_sdk_b2bi.types.update_partnership_request
    import aws_sdk_b2bi.types.update_partnership_response
    from aws_sdk_b2bi._services.async_b2bi import Asyncb2biClient, Asyncb2biClientConfig
    from aws_sdk_b2bi._services.b2bi import b2biClient, b2biClientConfig


class Partnership:
    def __init__(self, service: b2biClient) -> None:
        self._service = service

    def create(
        self,
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        name: "aws_sdk_b2bi.types.partner_name.PartnerName",
        email: "aws_sdk_b2bi.types.email.Email",
        capabilities: "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        phone: Optional["aws_sdk_b2bi.types.phone.Phone"] = None,
        capability_options: Optional[
            "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_b2bi.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_b2bi.types.create_partnership_response.CreatePartnershipResponse":
        """<p>Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            name: <p>Specifies a descriptive name for the partnership.</p>
            email: <p>Specifies the email address associated with this trading partner.</p>
            phone: <p>Specifies the phone number associated with the partnership.</p>
            capabilities: <p>Specifies a list of the capabilities associated with this partnership.</p>
            capability_options: <p>Specify the structure that contains the details for the associated capabilities.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Examples:
            Sample CreatePartnership call

            >>> client.create(capabilities=['ca-963a8121e4fc4e348'], client_token='foo', email='john@example.com', name='b2bipartner', phone='5555555555', profile_id='p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey1', 'Value': 'sampleValue1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.create_partnership_request.CreatePartnershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.create_partnership_response.CreatePartnershipResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.create_partnership

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.create_partnership.create_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.create_partnership_request.CreatePartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["name"] = name
        input_["email"] = email
        if phone is not None:
            input_["phone"] = phone
        input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options
        if client_token is not None:
            input_["client_token"] = client_token
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
        partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.get_partnership_response.GetPartnershipResponse":
        """<p>Retrieves the details for a partnership, based on the partner and profile IDs specified. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Examples:
            Sample GetPartnership call

            >>> client.read(partnership_id='ps-219fa02f5b4242af8')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.get_partnership_request.GetPartnershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.get_partnership_response.GetPartnershipResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.get_partnership

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.get_partnership.get_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.get_partnership_request.GetPartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["partnership_id"] = partnership_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        name: Optional["aws_sdk_b2bi.types.partner_name.PartnerName"] = None,
        capabilities: Optional[
            "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities"
        ] = None,
        capability_options: Optional[
            "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
    ) -> "aws_sdk_b2bi.types.update_partnership_response.UpdatePartnershipResponse":
        """<p>Updates some of the parameters for a partnership between a customer and trading partner. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>
            name: <p>The name of the partnership, used to identify it.</p>
            capabilities: <p>List of the capabilities associated with this partnership.</p>
            capability_options: <p>To update, specify the structure that contains the details for the associated capabilities.</p>

        Examples:
            Sample UpdatePartnership call

            >>> client.update(capabilities=['ca-963a8121e4fc4e348'], name='b2bipartner', partnership_id='ps-219fa02f5b4242af8')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.update_partnership_request.UpdatePartnershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.update_partnership_response.UpdatePartnershipResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.update_partnership

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.update_partnership.update_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.update_partnership_request.UpdatePartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["partnership_id"] = partnership_id
        if name is not None:
            input_["name"] = name
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Examples:
            Sample DeletePartnership call

            >>> client.delete(partnership_id='ps-219fa02f5b4242af8')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.delete_partnership_request.DeletePartnershipRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_b2bi._operations.b2_bi.delete_partnership

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.delete_partnership.delete_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.delete_partnership_request.DeletePartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["partnership_id"] = partnership_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        profile_id: Optional["aws_sdk_b2bi.types.profile_id.ProfileId"] = None,
        next_token: Optional["aws_sdk_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["aws_sdk_b2bi.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_b2bi.types.list_partnerships_response.ListPartnershipsResponse":
        """<p>Lists the partnerships associated with your Amazon Web Services account for your current or specified region. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Examples:
            Sample ListPartnerships call

            >>> client.list(max_results=50, next_token='foo', profile_id='p-60fbc37c87f04fce9')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.list_partnerships_request.ListPartnershipsRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.list_partnerships_response.ListPartnershipsResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.list_partnerships

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.list_partnerships.list_partnerships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.list_partnerships_request.ListPartnershipsRequest = {}  # type: ignore[typeddict-item]
        if profile_id is not None:
            input_["profile_id"] = profile_id
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


class AsyncPartnership:
    def __init__(self, service: Asyncb2biClient) -> None:
        self._service = service

    async def create(
        self,
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        name: "aws_sdk_b2bi.types.partner_name.PartnerName",
        email: "aws_sdk_b2bi.types.email.Email",
        capabilities: "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        phone: Optional["aws_sdk_b2bi.types.phone.Phone"] = None,
        capability_options: Optional[
            "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_b2bi.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_b2bi.types.create_partnership_response.CreatePartnershipResponse":
        """<p>Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            name: <p>Specifies a descriptive name for the partnership.</p>
            email: <p>Specifies the email address associated with this trading partner.</p>
            phone: <p>Specifies the phone number associated with the partnership.</p>
            capabilities: <p>Specifies a list of the capabilities associated with this partnership.</p>
            capability_options: <p>Specify the structure that contains the details for the associated capabilities.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Examples:
            Sample CreatePartnership call

            >>> await client.create(capabilities=['ca-963a8121e4fc4e348'], client_token='foo', email='john@example.com', name='b2bipartner', phone='5555555555', profile_id='p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey1', 'Value': 'sampleValue1'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.create_partnership_request.CreatePartnershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.create_partnership_response.CreatePartnershipResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.create_partnership

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.create_partnership.async_create_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.create_partnership_request.CreatePartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        input_["name"] = name
        input_["email"] = email
        if phone is not None:
            input_["phone"] = phone
        input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options
        if client_token is not None:
            input_["client_token"] = client_token
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
        partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.get_partnership_response.GetPartnershipResponse":
        """<p>Retrieves the details for a partnership, based on the partner and profile IDs specified. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Examples:
            Sample GetPartnership call

            >>> await client.read(partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.get_partnership_request.GetPartnershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.get_partnership_response.GetPartnershipResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.get_partnership

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.get_partnership.async_get_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.get_partnership_request.GetPartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["partnership_id"] = partnership_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["aws_sdk_b2bi.types.partner_name.PartnerName"] = None,
        capabilities: Optional[
            "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities"
        ] = None,
        capability_options: Optional[
            "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
    ) -> "aws_sdk_b2bi.types.update_partnership_response.UpdatePartnershipResponse":
        """<p>Updates some of the parameters for a partnership between a customer and trading partner. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>
            name: <p>The name of the partnership, used to identify it.</p>
            capabilities: <p>List of the capabilities associated with this partnership.</p>
            capability_options: <p>To update, specify the structure that contains the details for the associated capabilities.</p>

        Examples:
            Sample UpdatePartnership call

            >>> await client.update(capabilities=['ca-963a8121e4fc4e348'], name='b2bipartner', partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.update_partnership_request.UpdatePartnershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.update_partnership_response.UpdatePartnershipResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.update_partnership

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.update_partnership.async_update_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.update_partnership_request.UpdatePartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["partnership_id"] = partnership_id
        if name is not None:
            input_["name"] = name
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Examples:
            Sample DeletePartnership call

            >>> await client.delete(partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.delete_partnership_request.DeletePartnershipRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_b2bi._operations.b2_bi.delete_partnership

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.delete_partnership.async_delete_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.delete_partnership_request.DeletePartnershipRequest = {}  # type: ignore[typeddict-item]
        input_["partnership_id"] = partnership_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        profile_id: Optional["aws_sdk_b2bi.types.profile_id.ProfileId"] = None,
        next_token: Optional["aws_sdk_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["aws_sdk_b2bi.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_b2bi.types.list_partnerships_response.ListPartnershipsResponse":
        """<p>Lists the partnerships associated with your Amazon Web Services account for your current or specified region. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Examples:
            Sample ListPartnerships call

            >>> await client.list(max_results=50, next_token='foo', profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.list_partnerships_request.ListPartnershipsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.list_partnerships_response.ListPartnershipsResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.list_partnerships

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.list_partnerships.async_list_partnerships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.list_partnerships_request.ListPartnershipsRequest = {}  # type: ignore[typeddict-item]
        if profile_id is not None:
            input_["profile_id"] = profile_id
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
