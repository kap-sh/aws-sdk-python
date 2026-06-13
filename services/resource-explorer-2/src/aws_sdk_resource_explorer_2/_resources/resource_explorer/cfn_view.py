from typing import TYPE_CHECKING, Optional

import aws_sdk_resource_explorer_2._auth._signers
import aws_sdk_resource_explorer_2._auth._sigv4
from aws_sdk_resource_explorer_2._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.create_view_input
    import aws_sdk_resource_explorer_2.types.create_view_output
    import aws_sdk_resource_explorer_2.types.delete_view_input
    import aws_sdk_resource_explorer_2.types.delete_view_output
    import aws_sdk_resource_explorer_2.types.get_view_input
    import aws_sdk_resource_explorer_2.types.get_view_output
    import aws_sdk_resource_explorer_2.types.included_property_list
    import aws_sdk_resource_explorer_2.types.list_views_input
    import aws_sdk_resource_explorer_2.types.list_views_output
    import aws_sdk_resource_explorer_2.types.search_filter
    import aws_sdk_resource_explorer_2.types.tag_map
    import aws_sdk_resource_explorer_2.types.update_view_input
    import aws_sdk_resource_explorer_2.types.update_view_output
    import aws_sdk_resource_explorer_2.types.view_name
    from aws_sdk_resource_explorer_2._services.async_resource_explorer2 import (
        AsyncResourceExplorer2Client,
        AsyncResourceExplorer2ClientConfig,
    )
    from aws_sdk_resource_explorer_2._services.resource_explorer2 import (
        ResourceExplorer2Client,
        ResourceExplorer2ClientConfig,
    )


class CfnView:
    def __init__(self, service: ResourceExplorer2Client) -> None:
        self._service = service

    def create(
        self,
        view_name: "aws_sdk_resource_explorer_2.types.view_name.ViewName",
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
        client_token: Optional[str] = None,
        included_properties: Optional[
            "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
        ] = None,
        scope: Optional[str] = None,
        filters: Optional[
            "aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        tags: Optional["aws_sdk_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_resource_explorer_2.types.create_view_output.CreateViewOutput":
        """<p>Creates a view that users can query by using the <a>Search</a> operation. Results from queries that you make using this view include only resources that match the view's <code>Filters</code>. For more information about Amazon Web Services Resource Explorer views, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views.html\">Managing views</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <p>Only the principals with an IAM identity-based policy that grants <code>Allow</code> to the <code>Search</code> action on a <code>Resource</code> with the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of this view can <a>Search</a> using views you create with this operation.</p>

        Args:
            client_token: <p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID-type value</a> to ensure the uniqueness of your views.</p>
            view_name: <p>The name of the new view. This name appears in the list of views in Resource Explorer.</p> <p>The name must be no more than 64 characters long, and can include letters, digits, and the dash (-) character. The name must be unique within its Amazon Web Services Region.</p>
            included_properties: <p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>
            scope: <p>The root ARN of the account, an organizational unit (OU), or an organization ARN. If left empty, the default is account.</p>
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters\">filter prefixes</a> with optional <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators\">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
            tags: <p>Tag key and value pairs that are attached to the view.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resource_explorer_2.types.create_view_input.CreateViewInput]",
        ) -> OperationResponse[
            "aws_sdk_resource_explorer_2.types.create_view_output.CreateViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.create_view

            output, http_response = (
                aws_sdk_resource_explorer_2._operations.resource_explorer.create_view.create_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.create_view_input.CreateViewInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["view_name"] = view_name
        if included_properties is not None:
            input["included_properties"] = included_properties
        if scope is not None:
            input["scope"] = scope
        if filters is not None:
            input["filters"] = filters
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
        view_arn: str,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
    ) -> "aws_sdk_resource_explorer_2.types.get_view_output.GetViewOutput":
        """<p>Retrieves details of the specified view.</p>

        Args:
            view_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resource_explorer_2.types.get_view_input.GetViewInput]",
        ) -> OperationResponse[
            "aws_sdk_resource_explorer_2.types.get_view_output.GetViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_view

            output, http_response = (
                aws_sdk_resource_explorer_2._operations.resource_explorer.get_view.get_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.get_view_input.GetViewInput = {}  # type: ignore[typeddict-item]
        input["view_arn"] = view_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
        included_properties: Optional[
            "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
        ] = None,
        filters: Optional[
            "aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
    ) -> "aws_sdk_resource_explorer_2.types.update_view_output.UpdateViewOutput":
        """<p>Modifies some of the details of a view. You can change the filter string and the list of included properties. You can't change the name of the view.</p>

        Args:
            view_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want to modify.</p>
            included_properties: <p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters\">filter prefixes</a> with optional <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators\">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resource_explorer_2.types.update_view_input.UpdateViewInput]",
        ) -> OperationResponse[
            "aws_sdk_resource_explorer_2.types.update_view_output.UpdateViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.update_view

            output, http_response = (
                aws_sdk_resource_explorer_2._operations.resource_explorer.update_view.update_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.update_view_input.UpdateViewInput = {}  # type: ignore[typeddict-item]
        input["view_arn"] = view_arn
        if included_properties is not None:
            input["included_properties"] = included_properties
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
    ) -> "aws_sdk_resource_explorer_2.types.delete_view_output.DeleteViewOutput":
        """<p>Deletes the specified view.</p> <p>If the specified view is the default view for its Amazon Web Services Region, then all <a>Search</a> operations in that Region must explicitly specify the view to use until you configure a new default by calling the <a>AssociateDefaultView</a> operation.</p>

        Args:
            view_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resource_explorer_2.types.delete_view_input.DeleteViewInput]",
        ) -> OperationResponse[
            "aws_sdk_resource_explorer_2.types.delete_view_output.DeleteViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.delete_view

            output, http_response = (
                aws_sdk_resource_explorer_2._operations.resource_explorer.delete_view.delete_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.delete_view_input.DeleteViewInput = {}  # type: ignore[typeddict-item]
        input["view_arn"] = view_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_views_output.ListViewsOutput":
        """<p>Lists the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource names (ARNs)</a> of the views available in the Amazon Web Services Region in which you call this operation.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resource_explorer_2.types.list_views_input.ListViewsInput]",
        ) -> OperationResponse[
            "aws_sdk_resource_explorer_2.types.list_views_output.ListViewsOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_views

            output, http_response = (
                aws_sdk_resource_explorer_2._operations.resource_explorer.list_views.list_views(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.list_views_input.ListViewsInput = {}  # type: ignore[typeddict-item]
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


class AsyncCfnView:
    def __init__(self, service: AsyncResourceExplorer2Client) -> None:
        self._service = service

    async def create(
        self,
        view_name: "aws_sdk_resource_explorer_2.types.view_name.ViewName",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        client_token: Optional[str] = None,
        included_properties: Optional[
            "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
        ] = None,
        scope: Optional[str] = None,
        filters: Optional[
            "aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        tags: Optional["aws_sdk_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_resource_explorer_2.types.create_view_output.CreateViewOutput":
        """<p>Creates a view that users can query by using the <a>Search</a> operation. Results from queries that you make using this view include only resources that match the view's <code>Filters</code>. For more information about Amazon Web Services Resource Explorer views, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views.html\">Managing views</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <p>Only the principals with an IAM identity-based policy that grants <code>Allow</code> to the <code>Search</code> action on a <code>Resource</code> with the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of this view can <a>Search</a> using views you create with this operation.</p>

        Args:
            client_token: <p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID-type value</a> to ensure the uniqueness of your views.</p>
            view_name: <p>The name of the new view. This name appears in the list of views in Resource Explorer.</p> <p>The name must be no more than 64 characters long, and can include letters, digits, and the dash (-) character. The name must be unique within its Amazon Web Services Region.</p>
            included_properties: <p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>
            scope: <p>The root ARN of the account, an organizational unit (OU), or an organization ARN. If left empty, the default is account.</p>
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters\">filter prefixes</a> with optional <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators\">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
            tags: <p>Tag key and value pairs that are attached to the view.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.create_view_input.CreateViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.create_view_output.CreateViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.create_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.create_view.async_create_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.create_view_input.CreateViewInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["view_name"] = view_name
        if included_properties is not None:
            input["included_properties"] = included_properties
        if scope is not None:
            input["scope"] = scope
        if filters is not None:
            input["filters"] = filters
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
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "aws_sdk_resource_explorer_2.types.get_view_output.GetViewOutput":
        """<p>Retrieves details of the specified view.</p>

        Args:
            view_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.get_view_input.GetViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_view_output.GetViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_view.async_get_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.get_view_input.GetViewInput = {}  # type: ignore[typeddict-item]
        input["view_arn"] = view_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        included_properties: Optional[
            "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
        ] = None,
        filters: Optional[
            "aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
    ) -> "aws_sdk_resource_explorer_2.types.update_view_output.UpdateViewOutput":
        """<p>Modifies some of the details of a view. You can change the filter string and the list of included properties. You can't change the name of the view.</p>

        Args:
            view_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want to modify.</p>
            included_properties: <p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters\">filter prefixes</a> with optional <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators\">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.update_view_input.UpdateViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.update_view_output.UpdateViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.update_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.update_view.async_update_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.update_view_input.UpdateViewInput = {}  # type: ignore[typeddict-item]
        input["view_arn"] = view_arn
        if included_properties is not None:
            input["included_properties"] = included_properties
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "aws_sdk_resource_explorer_2.types.delete_view_output.DeleteViewOutput":
        """<p>Deletes the specified view.</p> <p>If the specified view is the default view for its Amazon Web Services Region, then all <a>Search</a> operations in that Region must explicitly specify the view to use until you configure a new default by calling the <a>AssociateDefaultView</a> operation.</p>

        Args:
            view_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.delete_view_input.DeleteViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.delete_view_output.DeleteViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.delete_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.delete_view.async_delete_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.delete_view_input.DeleteViewInput = {}  # type: ignore[typeddict-item]
        input["view_arn"] = view_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_views_output.ListViewsOutput":
        """<p>Lists the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource names (ARNs)</a> of the views available in the Amazon Web Services Region in which you call this operation.</p> <note> <p>Always check the <code>NextToken</code> response parameter for a <code>null</code> value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The <code>NextToken</code> response parameter value is <code>null</code> <i>only</i> when there are no more results to display.</p> </note>

        Args:
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_views_input.ListViewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_views_output.ListViewsOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_views

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_views.async_list_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_resource_explorer_2.types.list_views_input.ListViewsInput = {}  # type: ignore[typeddict-item]
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
