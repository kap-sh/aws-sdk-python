from typing import TYPE_CHECKING, Optional

from aws_sdk_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.create_repository_input
    import aws_sdk_proton.types.create_repository_output
    import aws_sdk_proton.types.delete_repository_input
    import aws_sdk_proton.types.delete_repository_output
    import aws_sdk_proton.types.get_repository_input
    import aws_sdk_proton.types.get_repository_output
    import aws_sdk_proton.types.list_repositories_input
    import aws_sdk_proton.types.list_repositories_output
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.repository_summary
    import aws_sdk_proton.types.tag_list
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class RepositoryResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        name: "aws_sdk_proton.types.repository_name.RepositoryName",
        connection_arn: "aws_sdk_proton.types.arn.Arn",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        encryption_key: Optional["aws_sdk_proton.types.arn.Arn"] = None,
        tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_proton.types.create_repository_output.CreateRepositoryOutput":
        """<p>Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html\">service-linked role</a> for you.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a>, <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles\">Template bundles</a>, and <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            connection_arn: <p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html\">Setting up for Proton</a> in the <i>Proton User Guide</i>.</p>
            encryption_key: <p>The ARN of your customer Amazon Web Services Key Management Service (Amazon Web Services KMS) key.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton repository. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.create_repository_input.CreateRepositoryInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.create_repository_output.CreateRepositoryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.create_repository

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.create_repository.create_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.create_repository_input.CreateRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["name"] = name
        input_["connection_arn"] = connection_arn
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
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
        provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        name: "aws_sdk_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_repository_output.GetRepositoryOutput":
        """<p>Get detail data for a linked repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name, for example <code>myrepos/myrepo</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.get_repository_input.GetRepositoryInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.get_repository_output.GetRepositoryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_repository

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.get_repository.get_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_repository_input.GetRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        name: "aws_sdk_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.delete_repository_output.DeleteRepositoryOutput":
        """<p>De-register and unlink your repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.delete_repository_input.DeleteRepositoryInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.delete_repository_output.DeleteRepositoryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_repository

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.delete_repository.delete_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.delete_repository_input.DeleteRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "aws_sdk_proton.types.list_repositories_output.ListRepositoriesOutput":
        """<p>List linked repositories with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.</p>
            max_results: <p>The maximum number of repositories to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_repositories_input.ListRepositoriesInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_repositories_output.ListRepositoriesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_repositories

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_repositories.list_repositories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_repositories_input.ListRepositoriesInput = {}  # type: ignore[typeddict-item]
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


class AsyncRepositoryResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        name: "aws_sdk_proton.types.repository_name.RepositoryName",
        connection_arn: "aws_sdk_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        encryption_key: Optional["aws_sdk_proton.types.arn.Arn"] = None,
        tags: Optional["aws_sdk_proton.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_proton.types.create_repository_output.CreateRepositoryOutput":
        """<p>Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html\">service-linked role</a> for you.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a>, <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles\">Template bundles</a>, and <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html\">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            connection_arn: <p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html\">Setting up for Proton</a> in the <i>Proton User Guide</i>.</p>
            encryption_key: <p>The ARN of your customer Amazon Web Services Key Management Service (Amazon Web Services KMS) key.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton repository. A tag is a key-value pair.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.create_repository_input.CreateRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.create_repository_output.CreateRepositoryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.create_repository

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.create_repository.async_create_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.create_repository_input.CreateRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["name"] = name
        input_["connection_arn"] = connection_arn
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
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
        provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        name: "aws_sdk_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_repository_output.GetRepositoryOutput":
        """<p>Get detail data for a linked repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name, for example <code>myrepos/myrepo</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_repository_input.GetRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_repository_output.GetRepositoryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_repository

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_repository.async_get_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_repository_input.GetRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        name: "aws_sdk_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.delete_repository_output.DeleteRepositoryOutput":
        """<p>De-register and unlink your repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.delete_repository_input.DeleteRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.delete_repository_output.DeleteRepositoryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.delete_repository

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.delete_repository.async_delete_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.delete_repository_input.DeleteRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["aws_sdk_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "aws_sdk_proton.types.list_repositories_output.ListRepositoriesOutput":
        """<p>List linked repositories with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.</p>
            max_results: <p>The maximum number of repositories to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_repositories_input.ListRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_repositories_output.ListRepositoriesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_repositories

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_repositories.async_list_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_repositories_input.ListRepositoriesInput = {}  # type: ignore[typeddict-item]
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
