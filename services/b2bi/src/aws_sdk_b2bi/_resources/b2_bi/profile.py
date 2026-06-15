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
    import aws_sdk_b2bi.types.business_name
    import aws_sdk_b2bi.types.create_profile_request
    import aws_sdk_b2bi.types.create_profile_response
    import aws_sdk_b2bi.types.delete_profile_request
    import aws_sdk_b2bi.types.email
    import aws_sdk_b2bi.types.get_profile_request
    import aws_sdk_b2bi.types.get_profile_response
    import aws_sdk_b2bi.types.list_profiles_request
    import aws_sdk_b2bi.types.list_profiles_response
    import aws_sdk_b2bi.types.logging
    import aws_sdk_b2bi.types.max_results
    import aws_sdk_b2bi.types.page_token
    import aws_sdk_b2bi.types.phone
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.profile_name
    import aws_sdk_b2bi.types.profile_summary
    import aws_sdk_b2bi.types.tag_list
    import aws_sdk_b2bi.types.update_profile_request
    import aws_sdk_b2bi.types.update_profile_response
    from aws_sdk_b2bi._services.async_b2bi import Asyncb2biClient, Asyncb2biClientConfig
    from aws_sdk_b2bi._services.b2bi import b2biClient, b2biClientConfig


class Profile:
    def __init__(self, service: b2biClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_b2bi.types.profile_name.ProfileName",
        phone: "aws_sdk_b2bi.types.phone.Phone",
        business_name: "aws_sdk_b2bi.types.business_name.BusinessName",
        logging: "aws_sdk_b2bi.types.logging.Logging",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        email: Optional["aws_sdk_b2bi.types.email.Email"] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_b2bi.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_b2bi.types.create_profile_response.CreateProfileResponse":
        """<p>Creates a customer profile. You can have up to five customer profiles, each representing a distinct private network. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            name: <p>Specifies the name of the profile.</p>
            email: <p>Specifies the email address associated with this customer profile.</p>
            phone: <p>Specifies the phone number associated with the profile.</p>
            business_name: <p>Specifies the name for the business associated with this profile.</p>
            logging: <p>Specifies whether or not logging is enabled for this profile.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Examples:
            Sample CreateProfile call

            >>> client.create(business_name="John's Shipping", client_token='foo', email='john@example.com', logging='ENABLED', name='Shipping Profile', phone='5555555555', tags=[{'Key': 'sampleKey', 'Value': 'sampleValue'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.create_profile_request.CreateProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.create_profile_response.CreateProfileResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.create_profile

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.create_profile.create_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.create_profile_request.CreateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if email is not None:
            input_["email"] = email
        input_["phone"] = phone
        input_["business_name"] = business_name
        input_["logging"] = logging
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
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.get_profile_response.GetProfileResponse":
        """<p>Retrieves the details for the profile specified by the profile ID. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>

        Examples:
            Sample GetProfile call

            >>> client.read(profile_id='p-60fbc37c87f04fce9')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.get_profile_request.GetProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.get_profile_response.GetProfileResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.get_profile

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.get_profile.get_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.get_profile_request.GetProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        name: Optional["aws_sdk_b2bi.types.profile_name.ProfileName"] = None,
        email: Optional["aws_sdk_b2bi.types.email.Email"] = None,
        phone: Optional["aws_sdk_b2bi.types.phone.Phone"] = None,
        business_name: Optional["aws_sdk_b2bi.types.business_name.BusinessName"] = None,
    ) -> "aws_sdk_b2bi.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates the specified parameters for a profile. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>
            name: <p>The name of the profile, used to identify it.</p>
            email: <p>Specifies the email address associated with this customer profile.</p>
            phone: <p>Specifies the phone number associated with the profile.</p>
            business_name: <p>Specifies the name for the business associated with this profile.</p>

        Examples:
            Sample UpdateProfile call

            >>> client.update(business_name="John's Shipping", email='john@example.com', name='Shipping Profile', phone='5555555555', profile_id='p-60fbc37c87f04fce9')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.update_profile_request.UpdateProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.update_profile_response.UpdateProfileResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.update_profile

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.update_profile.update_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.update_profile_request.UpdateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        if name is not None:
            input_["name"] = name
        if email is not None:
            input_["email"] = email
        if phone is not None:
            input_["phone"] = phone
        if business_name is not None:
            input_["business_name"] = business_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified profile. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>

        Examples:
            Sample DeleteProfile call

            >>> client.delete(profile_id='p-60fbc37c87f04fce9')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.delete_profile_request.DeleteProfileRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_b2bi._operations.b2_bi.delete_profile

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.delete_profile.delete_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.delete_profile_request.DeleteProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

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
        next_token: Optional["aws_sdk_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["aws_sdk_b2bi.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_b2bi.types.list_profiles_response.ListProfilesResponse":
        """<p>Lists the profiles associated with your Amazon Web Services account for your current or specified region. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of profiles to return.</p>

        Examples:
            Sample ListProfiles call

            >>> client.list(max_results=50, next_token='foo')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_b2bi.types.list_profiles_request.ListProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_b2bi.types.list_profiles_response.ListProfilesResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.list_profiles

            output, http_response = (
                aws_sdk_b2bi._operations.b2_bi.list_profiles.list_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.list_profiles_request.ListProfilesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncProfile:
    def __init__(self, service: Asyncb2biClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_b2bi.types.profile_name.ProfileName",
        phone: "aws_sdk_b2bi.types.phone.Phone",
        business_name: "aws_sdk_b2bi.types.business_name.BusinessName",
        logging: "aws_sdk_b2bi.types.logging.Logging",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        email: Optional["aws_sdk_b2bi.types.email.Email"] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_b2bi.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_b2bi.types.create_profile_response.CreateProfileResponse":
        """<p>Creates a customer profile. You can have up to five customer profiles, each representing a distinct private network. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            name: <p>Specifies the name of the profile.</p>
            email: <p>Specifies the email address associated with this customer profile.</p>
            phone: <p>Specifies the phone number associated with the profile.</p>
            business_name: <p>Specifies the name for the business associated with this profile.</p>
            logging: <p>Specifies whether or not logging is enabled for this profile.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Examples:
            Sample CreateProfile call

            >>> await client.create(business_name="John's Shipping", client_token='foo', email='john@example.com', logging='ENABLED', name='Shipping Profile', phone='5555555555', tags=[{'Key': 'sampleKey', 'Value': 'sampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.create_profile_request.CreateProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.create_profile_response.CreateProfileResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.create_profile

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.create_profile_request.CreateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if email is not None:
            input_["email"] = email
        input_["phone"] = phone
        input_["business_name"] = business_name
        input_["logging"] = logging
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
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "aws_sdk_b2bi.types.get_profile_response.GetProfileResponse":
        """<p>Retrieves the details for the profile specified by the profile ID. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>

        Examples:
            Sample GetProfile call

            >>> await client.read(profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.get_profile_request.GetProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.get_profile_response.GetProfileResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.get_profile

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.get_profile_request.GetProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["aws_sdk_b2bi.types.profile_name.ProfileName"] = None,
        email: Optional["aws_sdk_b2bi.types.email.Email"] = None,
        phone: Optional["aws_sdk_b2bi.types.phone.Phone"] = None,
        business_name: Optional["aws_sdk_b2bi.types.business_name.BusinessName"] = None,
    ) -> "aws_sdk_b2bi.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates the specified parameters for a profile. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>
            name: <p>The name of the profile, used to identify it.</p>
            email: <p>Specifies the email address associated with this customer profile.</p>
            phone: <p>Specifies the phone number associated with the profile.</p>
            business_name: <p>Specifies the name for the business associated with this profile.</p>

        Examples:
            Sample UpdateProfile call

            >>> await client.update(business_name="John's Shipping", email='john@example.com', name='Shipping Profile', phone='5555555555', profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.update_profile_request.UpdateProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.update_profile_response.UpdateProfileResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.update_profile

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.update_profile_request.UpdateProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id
        if name is not None:
            input_["name"] = name
        if email is not None:
            input_["email"] = email
        if phone is not None:
            input_["phone"] = phone
        if business_name is not None:
            input_["business_name"] = business_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified profile. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>

        Examples:
            Sample DeleteProfile call

            >>> await client.delete(profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.delete_profile_request.DeleteProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_b2bi._operations.b2_bi.delete_profile

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.delete_profile_request.DeleteProfileRequest = {}  # type: ignore[typeddict-item]
        input_["profile_id"] = profile_id

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
        next_token: Optional["aws_sdk_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["aws_sdk_b2bi.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_b2bi.types.list_profiles_response.ListProfilesResponse":
        """<p>Lists the profiles associated with your Amazon Web Services account for your current or specified region. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of profiles to return.</p>

        Examples:
            Sample ListProfiles call

            >>> await client.list(max_results=50, next_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_b2bi.types.list_profiles_request.ListProfilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_b2bi.types.list_profiles_response.ListProfilesResponse"
        ]:
            import aws_sdk_b2bi._operations.b2_bi.list_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_b2bi._operations.b2_bi.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_b2bi.types.list_profiles_request.ListProfilesRequest = {}  # type: ignore[typeddict-item]
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
