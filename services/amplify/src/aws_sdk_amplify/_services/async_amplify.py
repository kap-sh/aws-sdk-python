"""Generated from Smithy shape ``com.amazonaws.amplify#Amplify``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_amplify._auth._signers
import aws_sdk_amplify._auth._sigv4
from aws_sdk_amplify._auth._identity import Credentials
from aws_sdk_amplify._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_amplify._auth._zapros_handler import AuthMiddleware
from aws_sdk_amplify._pagination import resolve_path as _resolve_path
from aws_sdk_amplify._services._aws_config import aaws_config
from aws_sdk_amplify._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_amplify.types.access_token
    import aws_sdk_amplify.types.app
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.artifact_id
    import aws_sdk_amplify.types.auto_branch_creation_config
    import aws_sdk_amplify.types.auto_branch_creation_patterns
    import aws_sdk_amplify.types.auto_sub_domain_creation_patterns
    import aws_sdk_amplify.types.auto_sub_domain_iam_role
    import aws_sdk_amplify.types.backend
    import aws_sdk_amplify.types.backend_environment_arn
    import aws_sdk_amplify.types.basic_auth_credentials
    import aws_sdk_amplify.types.branch
    import aws_sdk_amplify.types.branch_name
    import aws_sdk_amplify.types.build_spec
    import aws_sdk_amplify.types.cache_config
    import aws_sdk_amplify.types.certificate_settings
    import aws_sdk_amplify.types.commit_id
    import aws_sdk_amplify.types.commit_message
    import aws_sdk_amplify.types.commit_time
    import aws_sdk_amplify.types.compute_role_arn
    import aws_sdk_amplify.types.create_app_request
    import aws_sdk_amplify.types.create_app_result
    import aws_sdk_amplify.types.create_backend_environment_request
    import aws_sdk_amplify.types.create_backend_environment_result
    import aws_sdk_amplify.types.create_branch_request
    import aws_sdk_amplify.types.create_branch_result
    import aws_sdk_amplify.types.create_deployment_request
    import aws_sdk_amplify.types.create_deployment_result
    import aws_sdk_amplify.types.create_domain_association_request
    import aws_sdk_amplify.types.create_domain_association_result
    import aws_sdk_amplify.types.create_webhook_request
    import aws_sdk_amplify.types.create_webhook_result
    import aws_sdk_amplify.types.custom_headers
    import aws_sdk_amplify.types.custom_rules
    import aws_sdk_amplify.types.delete_app_request
    import aws_sdk_amplify.types.delete_app_result
    import aws_sdk_amplify.types.delete_backend_environment_request
    import aws_sdk_amplify.types.delete_backend_environment_result
    import aws_sdk_amplify.types.delete_branch_request
    import aws_sdk_amplify.types.delete_branch_result
    import aws_sdk_amplify.types.delete_domain_association_request
    import aws_sdk_amplify.types.delete_domain_association_result
    import aws_sdk_amplify.types.delete_job_request
    import aws_sdk_amplify.types.delete_job_result
    import aws_sdk_amplify.types.delete_webhook_request
    import aws_sdk_amplify.types.delete_webhook_result
    import aws_sdk_amplify.types.deployment_artifacts
    import aws_sdk_amplify.types.description
    import aws_sdk_amplify.types.display_name
    import aws_sdk_amplify.types.domain_association
    import aws_sdk_amplify.types.domain_name
    import aws_sdk_amplify.types.enable_auto_branch_creation
    import aws_sdk_amplify.types.enable_auto_build
    import aws_sdk_amplify.types.enable_auto_sub_domain
    import aws_sdk_amplify.types.enable_basic_auth
    import aws_sdk_amplify.types.enable_branch_auto_build
    import aws_sdk_amplify.types.enable_branch_auto_deletion
    import aws_sdk_amplify.types.enable_notification
    import aws_sdk_amplify.types.enable_performance_mode
    import aws_sdk_amplify.types.enable_pull_request_preview
    import aws_sdk_amplify.types.enable_skew_protection
    import aws_sdk_amplify.types.end_time
    import aws_sdk_amplify.types.environment_name
    import aws_sdk_amplify.types.environment_variables
    import aws_sdk_amplify.types.file_map
    import aws_sdk_amplify.types.framework
    import aws_sdk_amplify.types.generate_access_logs_request
    import aws_sdk_amplify.types.generate_access_logs_result
    import aws_sdk_amplify.types.get_app_request
    import aws_sdk_amplify.types.get_app_result
    import aws_sdk_amplify.types.get_artifact_url_request
    import aws_sdk_amplify.types.get_artifact_url_result
    import aws_sdk_amplify.types.get_backend_environment_request
    import aws_sdk_amplify.types.get_backend_environment_result
    import aws_sdk_amplify.types.get_branch_request
    import aws_sdk_amplify.types.get_branch_result
    import aws_sdk_amplify.types.get_domain_association_request
    import aws_sdk_amplify.types.get_domain_association_result
    import aws_sdk_amplify.types.get_job_request
    import aws_sdk_amplify.types.get_job_result
    import aws_sdk_amplify.types.get_webhook_request
    import aws_sdk_amplify.types.get_webhook_result
    import aws_sdk_amplify.types.job_config
    import aws_sdk_amplify.types.job_id
    import aws_sdk_amplify.types.job_reason
    import aws_sdk_amplify.types.job_summary
    import aws_sdk_amplify.types.job_type
    import aws_sdk_amplify.types.list_apps_request
    import aws_sdk_amplify.types.list_apps_result
    import aws_sdk_amplify.types.list_artifacts_request
    import aws_sdk_amplify.types.list_artifacts_result
    import aws_sdk_amplify.types.list_backend_environments_request
    import aws_sdk_amplify.types.list_backend_environments_result
    import aws_sdk_amplify.types.list_branches_request
    import aws_sdk_amplify.types.list_branches_result
    import aws_sdk_amplify.types.list_domain_associations_request
    import aws_sdk_amplify.types.list_domain_associations_result
    import aws_sdk_amplify.types.list_jobs_request
    import aws_sdk_amplify.types.list_jobs_result
    import aws_sdk_amplify.types.list_tags_for_resource_request
    import aws_sdk_amplify.types.list_tags_for_resource_response
    import aws_sdk_amplify.types.list_webhooks_request
    import aws_sdk_amplify.types.list_webhooks_result
    import aws_sdk_amplify.types.max_results
    import aws_sdk_amplify.types.max_results_for_list_apps
    import aws_sdk_amplify.types.name
    import aws_sdk_amplify.types.next_token
    import aws_sdk_amplify.types.oauth_token
    import aws_sdk_amplify.types.platform
    import aws_sdk_amplify.types.pull_request_environment_name
    import aws_sdk_amplify.types.repository
    import aws_sdk_amplify.types.resource_arn
    import aws_sdk_amplify.types.service_role_arn
    import aws_sdk_amplify.types.source_url
    import aws_sdk_amplify.types.source_url_type
    import aws_sdk_amplify.types.stack_name
    import aws_sdk_amplify.types.stage
    import aws_sdk_amplify.types.start_deployment_request
    import aws_sdk_amplify.types.start_deployment_result
    import aws_sdk_amplify.types.start_job_request
    import aws_sdk_amplify.types.start_job_result
    import aws_sdk_amplify.types.start_time
    import aws_sdk_amplify.types.stop_job_request
    import aws_sdk_amplify.types.stop_job_result
    import aws_sdk_amplify.types.sub_domain_settings
    import aws_sdk_amplify.types.tag_key_list
    import aws_sdk_amplify.types.tag_map
    import aws_sdk_amplify.types.tag_resource_request
    import aws_sdk_amplify.types.tag_resource_response
    import aws_sdk_amplify.types.ttl
    import aws_sdk_amplify.types.untag_resource_request
    import aws_sdk_amplify.types.untag_resource_response
    import aws_sdk_amplify.types.update_app_request
    import aws_sdk_amplify.types.update_app_result
    import aws_sdk_amplify.types.update_branch_request
    import aws_sdk_amplify.types.update_branch_result
    import aws_sdk_amplify.types.update_domain_association_request
    import aws_sdk_amplify.types.update_domain_association_result
    import aws_sdk_amplify.types.update_webhook_request
    import aws_sdk_amplify.types.update_webhook_result
    import aws_sdk_amplify.types.webhook_id


class AsyncAmplifyClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncAmplifyClient:
    """A client for the ``Amplify`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncAmplifyClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncAmplifyClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAmplifyClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_app(
        self,
        name: "aws_sdk_amplify.types.name.Name",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        description: Optional["aws_sdk_amplify.types.description.Description"] = None,
        repository: Optional["aws_sdk_amplify.types.repository.Repository"] = None,
        platform: Optional["aws_sdk_amplify.types.platform.Platform"] = None,
        compute_role_arn: Optional[
            "aws_sdk_amplify.types.compute_role_arn.ComputeRoleArn"
        ] = None,
        iam_service_role_arn: Optional[
            "aws_sdk_amplify.types.service_role_arn.ServiceRoleArn"
        ] = None,
        oauth_token: Optional["aws_sdk_amplify.types.oauth_token.OauthToken"] = None,
        access_token: Optional["aws_sdk_amplify.types.access_token.AccessToken"] = None,
        environment_variables: Optional[
            "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
        ] = None,
        enable_branch_auto_build: Optional[
            "aws_sdk_amplify.types.enable_branch_auto_build.EnableBranchAutoBuild"
        ] = None,
        enable_branch_auto_deletion: Optional[
            "aws_sdk_amplify.types.enable_branch_auto_deletion.EnableBranchAutoDeletion"
        ] = None,
        enable_basic_auth: Optional[
            "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
        ] = None,
        basic_auth_credentials: Optional[
            "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
        ] = None,
        custom_rules: Optional["aws_sdk_amplify.types.custom_rules.CustomRules"] = None,
        tags: Optional["aws_sdk_amplify.types.tag_map.TagMap"] = None,
        build_spec: Optional["aws_sdk_amplify.types.build_spec.BuildSpec"] = None,
        custom_headers: Optional[
            "aws_sdk_amplify.types.custom_headers.CustomHeaders"
        ] = None,
        enable_auto_branch_creation: Optional[
            "aws_sdk_amplify.types.enable_auto_branch_creation.EnableAutoBranchCreation"
        ] = None,
        auto_branch_creation_patterns: Optional[
            "aws_sdk_amplify.types.auto_branch_creation_patterns.AutoBranchCreationPatterns"
        ] = None,
        auto_branch_creation_config: Optional[
            "aws_sdk_amplify.types.auto_branch_creation_config.AutoBranchCreationConfig"
        ] = None,
        job_config: Optional["aws_sdk_amplify.types.job_config.JobConfig"] = None,
        cache_config: Optional["aws_sdk_amplify.types.cache_config.CacheConfig"] = None,
    ) -> "aws_sdk_amplify.types.create_app_result.CreateAppResult":
        r"""<p>Creates a new Amplify app. </p>

        Args:
            name: <p>The name of the Amplify app. </p>
            description: <p>The description of the Amplify app. </p>
            repository: <p>The Git repository for the Amplify app. </p>
            platform: <p>The platform for the Amplify app. For a static app, set the platform type to <code>WEB</code>. For a dynamic server-side rendered (SSR) app, set the platform type to <code>WEB_COMPUTE</code>. For an app requiring Amplify Hosting's original SSR support only, set the platform type to <code>WEB_DYNAMIC</code>.</p> <p>If you are deploying an SSG only app with Next.js version 14 or later, you must set the platform type to <code>WEB_COMPUTE</code> and set the artifacts <code>baseDirectory</code> to <code>.next</code> in the application's build settings. For an example of the build specification settings, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/deploy-nextjs-app.html#build-setting-detection-ssg-14\">Amplify build settings for a Next.js 14 SSG application</a> in the <i>Amplify Hosting User Guide</i>.</p>
            compute_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to assign to an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html\">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>
            iam_service_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.</p>
            oauth_token: <p>The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.</p> <p>Use <code>oauthToken</code> for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use <code>accessToken</code>.</p> <p>You must specify either <code>oauthToken</code> or <code>accessToken</code> when you create a new app.</p> <p>Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth\">Migrating an existing OAuth app to the Amplify GitHub App</a> in the <i>Amplify User Guide</i> .</p>
            access_token: <p>The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.</p> <p>Use <code>accessToken</code> for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use <code>oauthToken</code>.</p> <p>You must specify either <code>accessToken</code> or <code>oauthToken</code> when you create a new app.</p> <p>Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth\">Migrating an existing OAuth app to the Amplify GitHub App</a> in the <i>Amplify User Guide</i> .</p>
            environment_variables: <p>The environment variables map for an Amplify app. </p> <p>For a list of the environment variables that are accessible to Amplify by default, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html\">Amplify Environment variables</a> in the <i>Amplify Hosting User Guide</i>.</p>
            enable_branch_auto_build: <p>Enables the auto building of branches for an Amplify app. </p>
            enable_branch_auto_deletion: <p>Automatically disconnects a branch in the Amplify console when you delete a branch from your Git repository. </p>
            enable_basic_auth: <p>Enables basic authorization for an Amplify app. This will apply to all branches that are part of this app. </p>
            basic_auth_credentials: <p>The credentials for basic authorization for an Amplify app. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>
            custom_rules: <p>The custom rewrite and redirect rules for an Amplify app. </p>
            tags: <p>The tag for an Amplify app. </p>
            build_spec: <p>The build specification (build spec) for an Amplify app. </p>
            custom_headers: <p>The custom HTTP headers for an Amplify app.</p>
            enable_auto_branch_creation: <p>Enables automated branch creation for an Amplify app. </p>
            auto_branch_creation_patterns: <p>The automated branch creation glob patterns for an Amplify app. </p>
            auto_branch_creation_config: <p>The automated branch creation configuration for an Amplify app. </p>
            job_config: <p>Describes the configuration details that apply to the jobs for an Amplify app.</p>
            cache_config: <p>The cache configuration for the Amplify app.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.create_app_request.CreateAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.create_app_result.CreateAppResult"
        ]:
            import aws_sdk_amplify._operations.amplify.create_app

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.create_app.async_create_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.create_app_request.CreateAppRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if repository is not None:
            input_["repository"] = repository
        if platform is not None:
            input_["platform"] = platform
        if compute_role_arn is not None:
            input_["compute_role_arn"] = compute_role_arn
        if iam_service_role_arn is not None:
            input_["iam_service_role_arn"] = iam_service_role_arn
        if oauth_token is not None:
            input_["oauth_token"] = oauth_token
        if access_token is not None:
            input_["access_token"] = access_token
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if enable_branch_auto_build is not None:
            input_["enable_branch_auto_build"] = enable_branch_auto_build
        if enable_branch_auto_deletion is not None:
            input_["enable_branch_auto_deletion"] = enable_branch_auto_deletion
        if enable_basic_auth is not None:
            input_["enable_basic_auth"] = enable_basic_auth
        if basic_auth_credentials is not None:
            input_["basic_auth_credentials"] = basic_auth_credentials
        if custom_rules is not None:
            input_["custom_rules"] = custom_rules
        if tags is not None:
            input_["tags"] = tags
        if build_spec is not None:
            input_["build_spec"] = build_spec
        if custom_headers is not None:
            input_["custom_headers"] = custom_headers
        if enable_auto_branch_creation is not None:
            input_["enable_auto_branch_creation"] = enable_auto_branch_creation
        if auto_branch_creation_patterns is not None:
            input_["auto_branch_creation_patterns"] = auto_branch_creation_patterns
        if auto_branch_creation_config is not None:
            input_["auto_branch_creation_config"] = auto_branch_creation_config
        if job_config is not None:
            input_["job_config"] = job_config
        if cache_config is not None:
            input_["cache_config"] = cache_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backend_environment(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        environment_name: "aws_sdk_amplify.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        stack_name: Optional["aws_sdk_amplify.types.stack_name.StackName"] = None,
        deployment_artifacts: Optional[
            "aws_sdk_amplify.types.deployment_artifacts.DeploymentArtifacts"
        ] = None,
    ) -> "aws_sdk_amplify.types.create_backend_environment_result.CreateBackendEnvironmentResult":
        """<p>Creates a new backend environment for an Amplify app. </p> <p>This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            environment_name: <p>The name for the backend environment. </p>
            stack_name: <p>The AWS CloudFormation stack name of a backend environment. </p>
            deployment_artifacts: <p>The name of deployment artifacts. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.create_backend_environment_request.CreateBackendEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.create_backend_environment_result.CreateBackendEnvironmentResult"
        ]:
            import aws_sdk_amplify._operations.amplify.create_backend_environment

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.create_backend_environment.async_create_backend_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.create_backend_environment_request.CreateBackendEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if deployment_artifacts is not None:
            input_["deployment_artifacts"] = deployment_artifacts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_branch(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        description: Optional["aws_sdk_amplify.types.description.Description"] = None,
        stage: Optional["aws_sdk_amplify.types.stage.Stage"] = None,
        framework: Optional["aws_sdk_amplify.types.framework.Framework"] = None,
        enable_notification: Optional[
            "aws_sdk_amplify.types.enable_notification.EnableNotification"
        ] = None,
        enable_auto_build: Optional[
            "aws_sdk_amplify.types.enable_auto_build.EnableAutoBuild"
        ] = None,
        enable_skew_protection: Optional[
            "aws_sdk_amplify.types.enable_skew_protection.EnableSkewProtection"
        ] = None,
        environment_variables: Optional[
            "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
        ] = None,
        basic_auth_credentials: Optional[
            "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
        ] = None,
        enable_basic_auth: Optional[
            "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
        ] = None,
        enable_performance_mode: Optional[
            "aws_sdk_amplify.types.enable_performance_mode.EnablePerformanceMode"
        ] = None,
        tags: Optional["aws_sdk_amplify.types.tag_map.TagMap"] = None,
        build_spec: Optional["aws_sdk_amplify.types.build_spec.BuildSpec"] = None,
        ttl: Optional["aws_sdk_amplify.types.ttl.TTL"] = None,
        display_name: Optional["aws_sdk_amplify.types.display_name.DisplayName"] = None,
        enable_pull_request_preview: Optional[
            "aws_sdk_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
        ] = None,
        pull_request_environment_name: Optional[
            "aws_sdk_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
        ] = None,
        backend_environment_arn: Optional[
            "aws_sdk_amplify.types.backend_environment_arn.BackendEnvironmentArn"
        ] = None,
        backend: Optional["aws_sdk_amplify.types.backend.Backend"] = None,
        compute_role_arn: Optional[
            "aws_sdk_amplify.types.compute_role_arn.ComputeRoleArn"
        ] = None,
    ) -> "aws_sdk_amplify.types.create_branch_result.CreateBranchResult":
        r"""<p> Creates a new branch for an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name for the branch. </p>
            description: <p>The description for the branch. </p>
            stage: <p>Describes the current stage for the branch. </p>
            framework: <p> The framework for the branch. </p>
            enable_notification: <p> Enables notifications for the branch. </p>
            enable_auto_build: <p> Enables auto building for the branch. </p>
            enable_skew_protection: <p>Specifies whether the skew protection feature is enabled for the branch.</p> <p>Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html\">Skew protection for Amplify deployments</a> in the <i>Amplify User Guide</i>.</p>
            environment_variables: <p> The environment variables for the branch. </p>
            basic_auth_credentials: <p> The basic authorization credentials for the branch. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>
            enable_basic_auth: <p> Enables basic authorization for the branch. </p>
            enable_performance_mode: <p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>
            tags: <p> The tag for the branch. </p>
            build_spec: <p> The build specification (build spec) for the branch. </p>
            ttl: <p> The content Time To Live (TTL) for the website in seconds. </p>
            display_name: <p> The display name for a branch. This is used as the default domain prefix. </p>
            enable_pull_request_preview: <p> Enables pull request previews for this branch. </p>
            pull_request_environment_name: <p> The Amplify environment name for the pull request. </p>
            backend_environment_arn: <p>The Amazon Resource Name (ARN) for a backend environment that is part of a Gen 1 Amplify app. </p> <p>This field is available to Amplify Gen 1 apps only where the backend is created using Amplify Studio or the Amplify command line interface (CLI).</p>
            backend: <p>The backend for a <code>Branch</code> of an Amplify app. Use for a backend created from an CloudFormation stack.</p> <p>This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>
            compute_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html\">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.create_branch_request.CreateBranchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.create_branch_result.CreateBranchResult"
        ]:
            import aws_sdk_amplify._operations.amplify.create_branch

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.create_branch.async_create_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.create_branch_request.CreateBranchRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        if description is not None:
            input_["description"] = description
        if stage is not None:
            input_["stage"] = stage
        if framework is not None:
            input_["framework"] = framework
        if enable_notification is not None:
            input_["enable_notification"] = enable_notification
        if enable_auto_build is not None:
            input_["enable_auto_build"] = enable_auto_build
        if enable_skew_protection is not None:
            input_["enable_skew_protection"] = enable_skew_protection
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if basic_auth_credentials is not None:
            input_["basic_auth_credentials"] = basic_auth_credentials
        if enable_basic_auth is not None:
            input_["enable_basic_auth"] = enable_basic_auth
        if enable_performance_mode is not None:
            input_["enable_performance_mode"] = enable_performance_mode
        if tags is not None:
            input_["tags"] = tags
        if build_spec is not None:
            input_["build_spec"] = build_spec
        if ttl is not None:
            input_["ttl"] = ttl
        if display_name is not None:
            input_["display_name"] = display_name
        if enable_pull_request_preview is not None:
            input_["enable_pull_request_preview"] = enable_pull_request_preview
        if pull_request_environment_name is not None:
            input_["pull_request_environment_name"] = pull_request_environment_name
        if backend_environment_arn is not None:
            input_["backend_environment_arn"] = backend_environment_arn
        if backend is not None:
            input_["backend"] = backend
        if compute_role_arn is not None:
            input_["compute_role_arn"] = compute_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_deployment(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        file_map: Optional["aws_sdk_amplify.types.file_map.FileMap"] = None,
    ) -> "aws_sdk_amplify.types.create_deployment_result.CreateDeploymentResult":
        """<p>Creates a deployment for a manually deployed Amplify app. Manually deployed apps are not connected to a Git repository. </p> <p>The maximum duration between the <code>CreateDeployment</code> call and the <code>StartDeployment</code> call cannot exceed 8 hours. If the duration exceeds 8 hours, the <code>StartDeployment</code> call and the associated <code>Job</code> will fail.</p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p> The name of the branch to use for the job. </p>
            file_map: <p> An optional file map that contains the file name as the key and the file content md5 hash as the value. If this argument is provided, the service will generate a unique upload URL per file. Otherwise, the service will only generate a single upload URL for the zipped files. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.create_deployment_result.CreateDeploymentResult"
        ]:
            import aws_sdk_amplify._operations.amplify.create_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.create_deployment_request.CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        if file_map is not None:
            input_["file_map"] = file_map

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_domain_association(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        domain_name: "aws_sdk_amplify.types.domain_name.DomainName",
        sub_domain_settings: "aws_sdk_amplify.types.sub_domain_settings.SubDomainSettings",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        enable_auto_sub_domain: Optional[
            "aws_sdk_amplify.types.enable_auto_sub_domain.EnableAutoSubDomain"
        ] = None,
        auto_sub_domain_creation_patterns: Optional[
            "aws_sdk_amplify.types.auto_sub_domain_creation_patterns.AutoSubDomainCreationPatterns"
        ] = None,
        auto_sub_domain_iam_role: Optional[
            "aws_sdk_amplify.types.auto_sub_domain_iam_role.AutoSubDomainIAMRole"
        ] = None,
        certificate_settings: Optional[
            "aws_sdk_amplify.types.certificate_settings.CertificateSettings"
        ] = None,
    ) -> "aws_sdk_amplify.types.create_domain_association_result.CreateDomainAssociationResult":
        """<p>Creates a new domain association for an Amplify app. This action associates a custom domain with the Amplify app </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            domain_name: <p> The domain name for the domain association. </p>
            enable_auto_sub_domain: <p> Enables the automated creation of subdomains for branches. </p>
            sub_domain_settings: <p> The setting for the subdomain. </p>
            auto_sub_domain_creation_patterns: <p> Sets the branch patterns for automatic subdomain creation. </p>
            auto_sub_domain_iam_role: <p> The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. </p>
            certificate_settings: <p>The type of SSL/TLS certificate to use for your custom domain. If you don't specify a certificate type, Amplify uses the default certificate that it provisions and manages for you.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.create_domain_association_request.CreateDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.create_domain_association_result.CreateDomainAssociationResult"
        ]:
            import aws_sdk_amplify._operations.amplify.create_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.create_domain_association.async_create_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.create_domain_association_request.CreateDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["domain_name"] = domain_name
        if enable_auto_sub_domain is not None:
            input_["enable_auto_sub_domain"] = enable_auto_sub_domain
        input_["sub_domain_settings"] = sub_domain_settings
        if auto_sub_domain_creation_patterns is not None:
            input_["auto_sub_domain_creation_patterns"] = (
                auto_sub_domain_creation_patterns
            )
        if auto_sub_domain_iam_role is not None:
            input_["auto_sub_domain_iam_role"] = auto_sub_domain_iam_role
        if certificate_settings is not None:
            input_["certificate_settings"] = certificate_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_webhook(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        description: Optional["aws_sdk_amplify.types.description.Description"] = None,
    ) -> "aws_sdk_amplify.types.create_webhook_result.CreateWebhookResult":
        """<p>Creates a new webhook on an Amplify app. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            branch_name: <p>The name for a branch that is part of an Amplify app. </p>
            description: <p>The description for a webhook. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.create_webhook_request.CreateWebhookRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.create_webhook_result.CreateWebhookResult"
        ]:
            import aws_sdk_amplify._operations.amplify.create_webhook

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.create_webhook.async_create_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.create_webhook_request.CreateWebhookRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.delete_app_result.DeleteAppResult":
        """<p>Deletes an existing Amplify app specified by an app ID. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.delete_app_request.DeleteAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.delete_app_result.DeleteAppResult"
        ]:
            import aws_sdk_amplify._operations.amplify.delete_app

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.delete_app.async_delete_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.delete_app_request.DeleteAppRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_backend_environment(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        environment_name: "aws_sdk_amplify.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.delete_backend_environment_result.DeleteBackendEnvironmentResult":
        """<p>Deletes a backend environment for an Amplify app. </p> <p>This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>

        Args:
            app_id: <p>The unique ID of an Amplify app. </p>
            environment_name: <p>The name of a backend environment of an Amplify app. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.delete_backend_environment_request.DeleteBackendEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.delete_backend_environment_result.DeleteBackendEnvironmentResult"
        ]:
            import aws_sdk_amplify._operations.amplify.delete_backend_environment

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.delete_backend_environment.async_delete_backend_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.delete_backend_environment_request.DeleteBackendEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_branch(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.delete_branch_result.DeleteBranchResult":
        """<p> Deletes a branch for an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.delete_branch_request.DeleteBranchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.delete_branch_result.DeleteBranchResult"
        ]:
            import aws_sdk_amplify._operations.amplify.delete_branch

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.delete_branch.async_delete_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.delete_branch_request.DeleteBranchRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_domain_association(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        domain_name: "aws_sdk_amplify.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.delete_domain_association_result.DeleteDomainAssociationResult":
        """<p>Deletes a domain association for an Amplify app. </p>

        Args:
            app_id: <p> The unique id for an Amplify app. </p>
            domain_name: <p> The name of the domain. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.delete_domain_association_request.DeleteDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.delete_domain_association_result.DeleteDomainAssociationResult"
        ]:
            import aws_sdk_amplify._operations.amplify.delete_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.delete_domain_association.async_delete_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.delete_domain_association_request.DeleteDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_job(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        job_id: "aws_sdk_amplify.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.delete_job_result.DeleteJobResult":
        """<p> Deletes a job for a branch of an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch to use for the job. </p>
            job_id: <p> The unique ID for the job. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.delete_job_result.DeleteJobResult"
        ]:
            import aws_sdk_amplify._operations.amplify.delete_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.delete_job_request.DeleteJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_webhook(
        self,
        webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.delete_webhook_result.DeleteWebhookResult":
        """<p>Deletes a webhook. </p>

        Args:
            webhook_id: <p>The unique ID for a webhook. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.delete_webhook_request.DeleteWebhookRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.delete_webhook_result.DeleteWebhookResult"
        ]:
            import aws_sdk_amplify._operations.amplify.delete_webhook

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.delete_webhook.async_delete_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.delete_webhook_request.DeleteWebhookRequest = {}  # type: ignore[typeddict-item]
        input_["webhook_id"] = webhook_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def generate_access_logs(
        self,
        domain_name: "aws_sdk_amplify.types.domain_name.DomainName",
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        start_time: Optional["aws_sdk_amplify.types.start_time.StartTime"] = None,
        end_time: Optional["aws_sdk_amplify.types.end_time.EndTime"] = None,
    ) -> "aws_sdk_amplify.types.generate_access_logs_result.GenerateAccessLogsResult":
        """<p>Returns the website access logs for a specific time range using a presigned URL. </p>

        Args:
            start_time: <p>The time at which the logs should start. The time range specified is inclusive of the start time. </p>
            end_time: <p>The time at which the logs should end. The time range specified is inclusive of the end time. </p>
            domain_name: <p>The name of the domain. </p>
            app_id: <p>The unique ID for an Amplify app. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.generate_access_logs_request.GenerateAccessLogsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.generate_access_logs_result.GenerateAccessLogsResult"
        ]:
            import aws_sdk_amplify._operations.amplify.generate_access_logs

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.generate_access_logs.async_generate_access_logs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.generate_access_logs_request.GenerateAccessLogsRequest = {}  # type: ignore[typeddict-item]
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        input_["domain_name"] = domain_name
        input_["app_id"] = app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_app(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.get_app_result.GetAppResult":
        """<p>Returns an existing Amplify app specified by an app ID.</p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_app_request.GetAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_app_result.GetAppResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_app

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_app.async_get_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_app_request.GetAppRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_artifact_url(
        self,
        artifact_id: "aws_sdk_amplify.types.artifact_id.ArtifactId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.get_artifact_url_result.GetArtifactUrlResult":
        """<p>Returns the artifact info that corresponds to an artifact id. </p>

        Args:
            artifact_id: <p>The unique ID for an artifact. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_artifact_url_request.GetArtifactUrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_artifact_url_result.GetArtifactUrlResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_artifact_url

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_artifact_url.async_get_artifact_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_artifact_url_request.GetArtifactUrlRequest = {}  # type: ignore[typeddict-item]
        input_["artifact_id"] = artifact_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend_environment(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        environment_name: "aws_sdk_amplify.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.get_backend_environment_result.GetBackendEnvironmentResult":
        """<p>Returns a backend environment for an Amplify app. </p> <p>This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>

        Args:
            app_id: <p>The unique id for an Amplify app. </p>
            environment_name: <p>The name for the backend environment. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_backend_environment_request.GetBackendEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_backend_environment_result.GetBackendEnvironmentResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_backend_environment

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_backend_environment.async_get_backend_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_backend_environment_request.GetBackendEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_branch(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.get_branch_result.GetBranchResult":
        """<p> Returns a branch for an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_branch_request.GetBranchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_branch_result.GetBranchResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_branch

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_branch.async_get_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_branch_request.GetBranchRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_domain_association(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        domain_name: "aws_sdk_amplify.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> (
        "aws_sdk_amplify.types.get_domain_association_result.GetDomainAssociationResult"
    ):
        """<p>Returns the domain information for an Amplify app. </p>

        Args:
            app_id: <p> The unique id for an Amplify app. </p>
            domain_name: <p> The name of the domain. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_domain_association_request.GetDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_domain_association_result.GetDomainAssociationResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_domain_association.async_get_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_domain_association_request.GetDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_job(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        job_id: "aws_sdk_amplify.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.get_job_result.GetJobResult":
        """<p> Returns a job for a branch of an Amplify app. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch to use for the job. </p>
            job_id: <p>The unique ID for the job. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_job_request.GetJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_job_result.GetJobResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_job.async_get_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_webhook(
        self,
        webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.get_webhook_result.GetWebhookResult":
        """<p>Returns the webhook information that corresponds to a specified webhook ID. </p>

        Args:
            webhook_id: <p>The unique ID for a webhook. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.get_webhook_request.GetWebhookRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.get_webhook_result.GetWebhookResult"
        ]:
            import aws_sdk_amplify._operations.amplify.get_webhook

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.get_webhook.async_get_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.get_webhook_request.GetWebhookRequest = {}  # type: ignore[typeddict-item]
        input_["webhook_id"] = webhook_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_apps(
        self,
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_amplify.types.max_results_for_list_apps.MaxResultsForListApps"
        ] = None,
    ) -> "aws_sdk_amplify.types.list_apps_result.ListAppsResult":
        """<p>Returns a list of the existing Amplify apps. </p>

        Args:
            next_token: <p>A pagination token. If non-null, the pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>
            max_results: <p>The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_apps_request.ListAppsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_apps_result.ListAppsResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_apps

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_apps.async_list_apps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_apps_request.ListAppsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_apps(
        self,
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_amplify.types.max_results_for_list_apps.MaxResultsForListApps"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_amplify.types.app.App]":
        _token = next_token
        while True:
            _response = await self.list_apps(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("apps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_artifacts(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        job_id: "aws_sdk_amplify.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_amplify.types.list_artifacts_result.ListArtifactsResult":
        r"""<p>Returns a list of end-to-end testing artifacts for a specified app, branch, and job.</p> <p>To return the build artifacts, use the <a href=\"https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetJob.html\">GetJob</a> API.</p> <p>For more information about Amplify testing support, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/running-tests.html\">Setting up end-to-end Cypress tests for your Amplify application</a> in the <i>Amplify Hosting User Guide</i>. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            branch_name: <p>The name of a branch that is part of an Amplify app. </p>
            job_id: <p>The unique ID for a job. </p>
            next_token: <p>A pagination token. Set to null to start listing artifacts from start. If a non-null pagination token is returned in a result, pass its value in here to list more artifacts. </p>
            max_results: <p>The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_artifacts_request.ListArtifactsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_artifacts_result.ListArtifactsResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_artifacts

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_artifacts.async_list_artifacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_artifacts_request.ListArtifactsRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        input_["job_id"] = job_id
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

    async def list_backend_environments(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        environment_name: Optional[
            "aws_sdk_amplify.types.environment_name.EnvironmentName"
        ] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_amplify.types.list_backend_environments_result.ListBackendEnvironmentsResult":
        """<p>Lists the backend environments for an Amplify app. </p> <p>This API is available only to Amplify Gen 1 applications where the backend is created using Amplify Studio or the Amplify command line interface (CLI). This API isn’t available to Amplify Gen 2 applications. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            environment_name: <p>The name of the backend environment </p>
            next_token: <p>A pagination token. Set to null to start listing backend environments from the start. If a non-null pagination token is returned in a result, pass its value in here to list more backend environments. </p>
            max_results: <p>The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_backend_environments_request.ListBackendEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_backend_environments_result.ListBackendEnvironmentsResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_backend_environments

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_backend_environments.async_list_backend_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_backend_environments_request.ListBackendEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        if environment_name is not None:
            input_["environment_name"] = environment_name
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

    async def list_branches(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_amplify.types.list_branches_result.ListBranchesResult":
        """<p> Lists the branches of an Amplify app. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            next_token: <p>A pagination token. Set to null to start listing branches from the start. If a non-null pagination token is returned in a result, pass its value in here to list more branches. </p>
            max_results: <p> The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_branches_request.ListBranchesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_branches_result.ListBranchesResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_branches

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_branches.async_list_branches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_branches_request.ListBranchesRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
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

    async def iter_list_branches(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_amplify.types.branch.Branch]":
        _token = next_token
        while True:
            _response = await self.list_branches(
                app_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("branches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_domain_associations(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_amplify.types.list_domain_associations_result.ListDomainAssociationsResult":
        """<p>Returns the domain associations for an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            next_token: <p> A pagination token. Set to null to start listing apps from the start. If non-null, a pagination token is returned in a result. Pass its value in here to list more projects. </p>
            max_results: <p> The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_domain_associations_request.ListDomainAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_domain_associations_result.ListDomainAssociationsResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_domain_associations

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_domain_associations.async_list_domain_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_domain_associations_request.ListDomainAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
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

    async def iter_list_domain_associations(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_amplify.types.domain_association.DomainAssociation]":
        _token = next_token
        while True:
            _response = await self.list_domain_associations(
                app_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("domain_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_jobs(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_amplify.types.list_jobs_result.ListJobsResult":
        """<p> Lists the jobs for a branch of an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch to use for the request. </p>
            next_token: <p>A pagination token. Set to null to start listing steps from the start. If a non-null pagination token is returned in a result, pass its value in here to list more steps. </p>
            max_results: <p>The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_jobs_result.ListJobsResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
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

    async def iter_list_jobs(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_amplify.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = await self.list_jobs(
                app_id,
                branch_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_amplify.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to list tags. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.resource_not_found_exception.ResourceNotFoundException: <p>An operation failed due to a non-existent resource. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_amplify._operations.amplify.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_webhooks(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        next_token: Optional["aws_sdk_amplify.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_amplify.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_amplify.types.list_webhooks_result.ListWebhooksResult":
        """<p>Returns a list of webhooks for an Amplify app. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            next_token: <p>A pagination token. Set to null to start listing webhooks from the start. If non-null,the pagination token is returned in a result. Pass its value in here to list more webhooks. </p>
            max_results: <p>The maximum number of records to list in a single response. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.list_webhooks_request.ListWebhooksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.list_webhooks_result.ListWebhooksResult"
        ]:
            import aws_sdk_amplify._operations.amplify.list_webhooks

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.list_webhooks.async_list_webhooks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.list_webhooks_request.ListWebhooksRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
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

    async def start_deployment(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        job_id: Optional["aws_sdk_amplify.types.job_id.JobId"] = None,
        source_url: Optional["aws_sdk_amplify.types.source_url.SourceUrl"] = None,
        source_url_type: Optional[
            "aws_sdk_amplify.types.source_url_type.SourceUrlType"
        ] = None,
    ) -> "aws_sdk_amplify.types.start_deployment_result.StartDeploymentResult":
        """<p>Starts a deployment for a manually deployed app. Manually deployed apps are not connected to a Git repository. </p> <p>The maximum duration between the <code>CreateDeployment</code> call and the <code>StartDeployment</code> call cannot exceed 8 hours. If the duration exceeds 8 hours, the <code>StartDeployment</code> call and the associated <code>Job</code> will fail.</p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch to use for the deployment job. </p>
            job_id: <p>The job ID for this deployment that is generated by the <code>CreateDeployment</code> request. </p>
            source_url: <p>The source URL for the deployment that is used when calling <code>StartDeployment</code> without <code>CreateDeployment</code>. The source URL can be either an HTTP GET URL that is publicly accessible and downloads a single .zip file, or an Amazon S3 bucket and prefix.</p>
            source_url_type: <p>The type of source specified by the <code>sourceURL</code>. If the value is <code>ZIP</code>, the source is a .zip file. If the value is <code>BUCKET_PREFIX</code>, the source is an Amazon S3 bucket and prefix. If no value is specified, the default is <code>ZIP</code>.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.start_deployment_request.StartDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.start_deployment_result.StartDeploymentResult"
        ]:
            import aws_sdk_amplify._operations.amplify.start_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.start_deployment.async_start_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.start_deployment_request.StartDeploymentRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        if job_id is not None:
            input_["job_id"] = job_id
        if source_url is not None:
            input_["source_url"] = source_url
        if source_url_type is not None:
            input_["source_url_type"] = source_url_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_job(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        job_type: "aws_sdk_amplify.types.job_type.JobType",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        job_id: Optional["aws_sdk_amplify.types.job_id.JobId"] = None,
        job_reason: Optional["aws_sdk_amplify.types.job_reason.JobReason"] = None,
        commit_id: Optional["aws_sdk_amplify.types.commit_id.CommitId"] = None,
        commit_message: Optional[
            "aws_sdk_amplify.types.commit_message.CommitMessage"
        ] = None,
        commit_time: Optional["aws_sdk_amplify.types.commit_time.CommitTime"] = None,
    ) -> "aws_sdk_amplify.types.start_job_result.StartJobResult":
        """<p> Starts a new job for a branch of an Amplify app. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch to use for the job. </p>
            job_id: <p>The unique ID for an existing job. This is required if the value of <code>jobType</code> is <code>RETRY</code>. </p>
            job_type: <p>Describes the type for the job. The job type <code>RELEASE</code> starts a new job with the latest change from the specified branch. This value is available only for apps that are connected to a repository. </p> <p>The job type <code>RETRY</code> retries an existing job. If the job type value is <code>RETRY</code>, the <code>jobId</code> is also required. </p>
            job_reason: <p>A descriptive reason for starting the job.</p>
            commit_id: <p> The commit ID from a third-party repository provider for the job. </p>
            commit_message: <p> The commit message from a third-party repository provider for the job. </p>
            commit_time: <p> The commit date and time for the job. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.start_job_request.StartJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.start_job_result.StartJobResult"
        ]:
            import aws_sdk_amplify._operations.amplify.start_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.start_job.async_start_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.start_job_request.StartJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        if job_id is not None:
            input_["job_id"] = job_id
        input_["job_type"] = job_type
        if job_reason is not None:
            input_["job_reason"] = job_reason
        if commit_id is not None:
            input_["commit_id"] = commit_id
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if commit_time is not None:
            input_["commit_time"] = commit_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_job(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        job_id: "aws_sdk_amplify.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.stop_job_result.StopJobResult":
        """<p> Stops a job that is in progress for a branch of an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch to use for the stop job request. </p>
            job_id: <p> The unique id for the job. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.limit_exceeded_exception.LimitExceededException: <p>A resource could not be created because service quotas were exceeded. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.stop_job_request.StopJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.stop_job_result.StopJobResult"
        ]:
            import aws_sdk_amplify._operations.amplify.stop_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.stop_job.async_stop_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.stop_job_request.StopJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_amplify.types.resource_arn.ResourceArn",
        tags: "aws_sdk_amplify.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.tag_resource_response.TagResourceResponse":
        """<p>Tags the resource with a tag key and value.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) to use to tag a resource. </p>
            tags: <p>The tags used to tag the resource. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.resource_not_found_exception.ResourceNotFoundException: <p>An operation failed due to a non-existent resource. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_amplify._operations.amplify.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_amplify.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_amplify.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
    ) -> "aws_sdk_amplify.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource with a specified Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to untag a resource. </p>
            tag_keys: <p>The tag keys to use to untag a resource. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.resource_not_found_exception.ResourceNotFoundException: <p>An operation failed due to a non-existent resource. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_amplify._operations.amplify.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_app(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        name: Optional["aws_sdk_amplify.types.name.Name"] = None,
        description: Optional["aws_sdk_amplify.types.description.Description"] = None,
        platform: Optional["aws_sdk_amplify.types.platform.Platform"] = None,
        compute_role_arn: Optional[
            "aws_sdk_amplify.types.compute_role_arn.ComputeRoleArn"
        ] = None,
        iam_service_role_arn: Optional[
            "aws_sdk_amplify.types.service_role_arn.ServiceRoleArn"
        ] = None,
        environment_variables: Optional[
            "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
        ] = None,
        enable_branch_auto_build: Optional[
            "aws_sdk_amplify.types.enable_auto_build.EnableAutoBuild"
        ] = None,
        enable_branch_auto_deletion: Optional[
            "aws_sdk_amplify.types.enable_branch_auto_deletion.EnableBranchAutoDeletion"
        ] = None,
        enable_basic_auth: Optional[
            "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
        ] = None,
        basic_auth_credentials: Optional[
            "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
        ] = None,
        custom_rules: Optional["aws_sdk_amplify.types.custom_rules.CustomRules"] = None,
        build_spec: Optional["aws_sdk_amplify.types.build_spec.BuildSpec"] = None,
        custom_headers: Optional[
            "aws_sdk_amplify.types.custom_headers.CustomHeaders"
        ] = None,
        enable_auto_branch_creation: Optional[
            "aws_sdk_amplify.types.enable_auto_branch_creation.EnableAutoBranchCreation"
        ] = None,
        auto_branch_creation_patterns: Optional[
            "aws_sdk_amplify.types.auto_branch_creation_patterns.AutoBranchCreationPatterns"
        ] = None,
        auto_branch_creation_config: Optional[
            "aws_sdk_amplify.types.auto_branch_creation_config.AutoBranchCreationConfig"
        ] = None,
        repository: Optional["aws_sdk_amplify.types.repository.Repository"] = None,
        oauth_token: Optional["aws_sdk_amplify.types.oauth_token.OauthToken"] = None,
        access_token: Optional["aws_sdk_amplify.types.access_token.AccessToken"] = None,
        job_config: Optional["aws_sdk_amplify.types.job_config.JobConfig"] = None,
        cache_config: Optional["aws_sdk_amplify.types.cache_config.CacheConfig"] = None,
    ) -> "aws_sdk_amplify.types.update_app_result.UpdateAppResult":
        r"""<p>Updates an existing Amplify app. </p>

        Args:
            app_id: <p>The unique ID for an Amplify app. </p>
            name: <p>The name for an Amplify app. </p>
            description: <p>The description for an Amplify app. </p>
            platform: <p>The platform for the Amplify app. For a static app, set the platform type to <code>WEB</code>. For a dynamic server-side rendered (SSR) app, set the platform type to <code>WEB_COMPUTE</code>. For an app requiring Amplify Hosting's original SSR support only, set the platform type to <code>WEB_DYNAMIC</code>.</p> <p>If you are deploying an SSG only app with Next.js version 14 or later, you must set the platform type to <code>WEB_COMPUTE</code>.</p>
            compute_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to assign to an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html\">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>
            iam_service_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.</p>
            environment_variables: <p>The environment variables for an Amplify app. </p>
            enable_branch_auto_build: <p>Enables branch auto-building for an Amplify app. </p>
            enable_branch_auto_deletion: <p>Automatically disconnects a branch in the Amplify console when you delete a branch from your Git repository. </p>
            enable_basic_auth: <p>Enables basic authorization for an Amplify app. </p>
            basic_auth_credentials: <p>The basic authorization credentials for an Amplify app. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>
            custom_rules: <p>The custom redirect and rewrite rules for an Amplify app. </p>
            build_spec: <p>The build specification (build spec) for an Amplify app. </p>
            custom_headers: <p>The custom HTTP headers for an Amplify app.</p>
            enable_auto_branch_creation: <p>Enables automated branch creation for an Amplify app. </p>
            auto_branch_creation_patterns: <p>Describes the automated branch creation glob patterns for an Amplify app. </p>
            auto_branch_creation_config: <p>The automated branch creation configuration for an Amplify app. </p>
            repository: <p>The name of the Git repository for an Amplify app.</p>
            oauth_token: <p>The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.</p> <p>Use <code>oauthToken</code> for repository providers other than GitHub, such as Bitbucket or CodeCommit.</p> <p>To authorize access to GitHub as your repository provider, use <code>accessToken</code>.</p> <p>You must specify either <code>oauthToken</code> or <code>accessToken</code> when you update an app.</p> <p>Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth\">Migrating an existing OAuth app to the Amplify GitHub App</a> in the <i>Amplify User Guide</i> .</p>
            access_token: <p>The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.</p> <p>Use <code>accessToken</code> for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use <code>oauthToken</code>.</p> <p>You must specify either <code>accessToken</code> or <code>oauthToken</code> when you update an app.</p> <p>Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth\">Migrating an existing OAuth app to the Amplify GitHub App</a> in the <i>Amplify User Guide</i> .</p>
            job_config: <p>Describes the configuration details that apply to the jobs for an Amplify app.</p>
            cache_config: <p>The cache configuration for the Amplify app.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.update_app_request.UpdateAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.update_app_result.UpdateAppResult"
        ]:
            import aws_sdk_amplify._operations.amplify.update_app

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.update_app.async_update_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.update_app_request.UpdateAppRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if platform is not None:
            input_["platform"] = platform
        if compute_role_arn is not None:
            input_["compute_role_arn"] = compute_role_arn
        if iam_service_role_arn is not None:
            input_["iam_service_role_arn"] = iam_service_role_arn
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if enable_branch_auto_build is not None:
            input_["enable_branch_auto_build"] = enable_branch_auto_build
        if enable_branch_auto_deletion is not None:
            input_["enable_branch_auto_deletion"] = enable_branch_auto_deletion
        if enable_basic_auth is not None:
            input_["enable_basic_auth"] = enable_basic_auth
        if basic_auth_credentials is not None:
            input_["basic_auth_credentials"] = basic_auth_credentials
        if custom_rules is not None:
            input_["custom_rules"] = custom_rules
        if build_spec is not None:
            input_["build_spec"] = build_spec
        if custom_headers is not None:
            input_["custom_headers"] = custom_headers
        if enable_auto_branch_creation is not None:
            input_["enable_auto_branch_creation"] = enable_auto_branch_creation
        if auto_branch_creation_patterns is not None:
            input_["auto_branch_creation_patterns"] = auto_branch_creation_patterns
        if auto_branch_creation_config is not None:
            input_["auto_branch_creation_config"] = auto_branch_creation_config
        if repository is not None:
            input_["repository"] = repository
        if oauth_token is not None:
            input_["oauth_token"] = oauth_token
        if access_token is not None:
            input_["access_token"] = access_token
        if job_config is not None:
            input_["job_config"] = job_config
        if cache_config is not None:
            input_["cache_config"] = cache_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_branch(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        branch_name: "aws_sdk_amplify.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        description: Optional["aws_sdk_amplify.types.description.Description"] = None,
        framework: Optional["aws_sdk_amplify.types.framework.Framework"] = None,
        stage: Optional["aws_sdk_amplify.types.stage.Stage"] = None,
        enable_notification: Optional[
            "aws_sdk_amplify.types.enable_notification.EnableNotification"
        ] = None,
        enable_auto_build: Optional[
            "aws_sdk_amplify.types.enable_auto_build.EnableAutoBuild"
        ] = None,
        enable_skew_protection: Optional[
            "aws_sdk_amplify.types.enable_skew_protection.EnableSkewProtection"
        ] = None,
        environment_variables: Optional[
            "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
        ] = None,
        basic_auth_credentials: Optional[
            "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
        ] = None,
        enable_basic_auth: Optional[
            "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
        ] = None,
        enable_performance_mode: Optional[
            "aws_sdk_amplify.types.enable_performance_mode.EnablePerformanceMode"
        ] = None,
        build_spec: Optional["aws_sdk_amplify.types.build_spec.BuildSpec"] = None,
        ttl: Optional["aws_sdk_amplify.types.ttl.TTL"] = None,
        display_name: Optional["aws_sdk_amplify.types.display_name.DisplayName"] = None,
        enable_pull_request_preview: Optional[
            "aws_sdk_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
        ] = None,
        pull_request_environment_name: Optional[
            "aws_sdk_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
        ] = None,
        backend_environment_arn: Optional[
            "aws_sdk_amplify.types.backend_environment_arn.BackendEnvironmentArn"
        ] = None,
        backend: Optional["aws_sdk_amplify.types.backend.Backend"] = None,
        compute_role_arn: Optional[
            "aws_sdk_amplify.types.compute_role_arn.ComputeRoleArn"
        ] = None,
    ) -> "aws_sdk_amplify.types.update_branch_result.UpdateBranchResult":
        r"""<p> Updates a branch for an Amplify app. </p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            branch_name: <p>The name of the branch. </p>
            description: <p> The description for the branch. </p>
            framework: <p> The framework for the branch. </p>
            stage: <p> Describes the current stage for the branch. </p>
            enable_notification: <p> Enables notifications for the branch. </p>
            enable_auto_build: <p> Enables auto building for the branch. </p>
            enable_skew_protection: <p>Specifies whether the skew protection feature is enabled for the branch.</p> <p>Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html\">Skew protection for Amplify deployments</a> in the <i>Amplify User Guide</i>.</p>
            environment_variables: <p> The environment variables for the branch. </p>
            basic_auth_credentials: <p> The basic authorization credentials for the branch. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>
            enable_basic_auth: <p> Enables basic authorization for the branch. </p>
            enable_performance_mode: <p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>
            build_spec: <p> The build specification (build spec) for the branch. </p>
            ttl: <p> The content Time to Live (TTL) for the website in seconds. </p>
            display_name: <p> The display name for a branch. This is used as the default domain prefix. </p>
            enable_pull_request_preview: <p> Enables pull request previews for this branch. </p>
            pull_request_environment_name: <p> The Amplify environment name for the pull request. </p>
            backend_environment_arn: <p>The Amazon Resource Name (ARN) for a backend environment that is part of a Gen 1 Amplify app. </p> <p>This field is available to Amplify Gen 1 apps only where the backend is created using Amplify Studio or the Amplify command line interface (CLI).</p>
            backend: <p>The backend for a <code>Branch</code> of an Amplify app. Use for a backend created from an CloudFormation stack.</p> <p>This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>
            compute_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html\">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.update_branch_request.UpdateBranchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.update_branch_result.UpdateBranchResult"
        ]:
            import aws_sdk_amplify._operations.amplify.update_branch

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.update_branch.async_update_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.update_branch_request.UpdateBranchRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["branch_name"] = branch_name
        if description is not None:
            input_["description"] = description
        if framework is not None:
            input_["framework"] = framework
        if stage is not None:
            input_["stage"] = stage
        if enable_notification is not None:
            input_["enable_notification"] = enable_notification
        if enable_auto_build is not None:
            input_["enable_auto_build"] = enable_auto_build
        if enable_skew_protection is not None:
            input_["enable_skew_protection"] = enable_skew_protection
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if basic_auth_credentials is not None:
            input_["basic_auth_credentials"] = basic_auth_credentials
        if enable_basic_auth is not None:
            input_["enable_basic_auth"] = enable_basic_auth
        if enable_performance_mode is not None:
            input_["enable_performance_mode"] = enable_performance_mode
        if build_spec is not None:
            input_["build_spec"] = build_spec
        if ttl is not None:
            input_["ttl"] = ttl
        if display_name is not None:
            input_["display_name"] = display_name
        if enable_pull_request_preview is not None:
            input_["enable_pull_request_preview"] = enable_pull_request_preview
        if pull_request_environment_name is not None:
            input_["pull_request_environment_name"] = pull_request_environment_name
        if backend_environment_arn is not None:
            input_["backend_environment_arn"] = backend_environment_arn
        if backend is not None:
            input_["backend"] = backend
        if compute_role_arn is not None:
            input_["compute_role_arn"] = compute_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_domain_association(
        self,
        app_id: "aws_sdk_amplify.types.app_id.AppId",
        domain_name: "aws_sdk_amplify.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        enable_auto_sub_domain: Optional[
            "aws_sdk_amplify.types.enable_auto_sub_domain.EnableAutoSubDomain"
        ] = None,
        sub_domain_settings: Optional[
            "aws_sdk_amplify.types.sub_domain_settings.SubDomainSettings"
        ] = None,
        auto_sub_domain_creation_patterns: Optional[
            "aws_sdk_amplify.types.auto_sub_domain_creation_patterns.AutoSubDomainCreationPatterns"
        ] = None,
        auto_sub_domain_iam_role: Optional[
            "aws_sdk_amplify.types.auto_sub_domain_iam_role.AutoSubDomainIAMRole"
        ] = None,
        certificate_settings: Optional[
            "aws_sdk_amplify.types.certificate_settings.CertificateSettings"
        ] = None,
    ) -> "aws_sdk_amplify.types.update_domain_association_result.UpdateDomainAssociationResult":
        """<p>Creates a new domain association for an Amplify app.</p>

        Args:
            app_id: <p> The unique ID for an Amplify app. </p>
            domain_name: <p> The name of the domain. </p>
            enable_auto_sub_domain: <p> Enables the automated creation of subdomains for branches. </p>
            sub_domain_settings: <p> Describes the settings for the subdomain. </p>
            auto_sub_domain_creation_patterns: <p> Sets the branch patterns for automatic subdomain creation. </p>
            auto_sub_domain_iam_role: <p> The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. </p>
            certificate_settings: <p>The type of SSL/TLS certificate to use for your custom domain.</p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.update_domain_association_request.UpdateDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.update_domain_association_result.UpdateDomainAssociationResult"
        ]:
            import aws_sdk_amplify._operations.amplify.update_domain_association

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.update_domain_association.async_update_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.update_domain_association_request.UpdateDomainAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["domain_name"] = domain_name
        if enable_auto_sub_domain is not None:
            input_["enable_auto_sub_domain"] = enable_auto_sub_domain
        if sub_domain_settings is not None:
            input_["sub_domain_settings"] = sub_domain_settings
        if auto_sub_domain_creation_patterns is not None:
            input_["auto_sub_domain_creation_patterns"] = (
                auto_sub_domain_creation_patterns
            )
        if auto_sub_domain_iam_role is not None:
            input_["auto_sub_domain_iam_role"] = auto_sub_domain_iam_role
        if certificate_settings is not None:
            input_["certificate_settings"] = certificate_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_webhook(
        self,
        webhook_id: "aws_sdk_amplify.types.webhook_id.WebhookId",
        *,
        config_overrides: Optional[AsyncAmplifyClientConfig] = None,
        branch_name: Optional["aws_sdk_amplify.types.branch_name.BranchName"] = None,
        description: Optional["aws_sdk_amplify.types.description.Description"] = None,
    ) -> "aws_sdk_amplify.types.update_webhook_result.UpdateWebhookResult":
        """<p>Updates a webhook. </p>

        Args:
            webhook_id: <p>The unique ID for a webhook. </p>
            branch_name: <p>The name for a branch that is part of an Amplify app. </p>
            description: <p>The description for a webhook. </p>

        Raises:
            aws_sdk_amplify.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data. </p>
            aws_sdk_amplify.errors.dependent_service_failure_exception.DependentServiceFailureException: <p>An operation failed because a dependent service threw an exception. </p>
            aws_sdk_amplify.errors.internal_failure_exception.InternalFailureException: <p>The service failed to perform an operation due to an internal issue. </p>
            aws_sdk_amplify.errors.not_found_exception.NotFoundException: <p>An entity was not found during an operation. </p>
            aws_sdk_amplify.errors.unauthorized_exception.UnauthorizedException: <p>An operation failed due to a lack of access. </p>
            aws_sdk_amplify.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplify.types.update_webhook_request.UpdateWebhookRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplify.types.update_webhook_result.UpdateWebhookResult"
        ]:
            import aws_sdk_amplify._operations.amplify.update_webhook

            (
                output,
                http_response,
            ) = await aws_sdk_amplify._operations.amplify.update_webhook.async_update_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_amplify.types.update_webhook_request.UpdateWebhookRequest = {}  # type: ignore[typeddict-item]
        input_["webhook_id"] = webhook_id
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
