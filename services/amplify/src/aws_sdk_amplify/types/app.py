"""Generated from Smithy shape ``com.amazonaws.amplify#App``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.app_arn
    import aws_sdk_amplify.types.app_id
    import aws_sdk_amplify.types.auto_branch_creation_config
    import aws_sdk_amplify.types.auto_branch_creation_patterns
    import aws_sdk_amplify.types.basic_auth_credentials
    import aws_sdk_amplify.types.build_spec
    import aws_sdk_amplify.types.cache_config
    import aws_sdk_amplify.types.compute_role_arn
    import aws_sdk_amplify.types.create_time
    import aws_sdk_amplify.types.custom_headers
    import aws_sdk_amplify.types.custom_rules
    import aws_sdk_amplify.types.default_domain
    import aws_sdk_amplify.types.description
    import aws_sdk_amplify.types.enable_auto_branch_creation
    import aws_sdk_amplify.types.enable_basic_auth
    import aws_sdk_amplify.types.enable_branch_auto_build
    import aws_sdk_amplify.types.enable_branch_auto_deletion
    import aws_sdk_amplify.types.environment_variables
    import aws_sdk_amplify.types.job_config
    import aws_sdk_amplify.types.name
    import aws_sdk_amplify.types.platform
    import aws_sdk_amplify.types.production_branch
    import aws_sdk_amplify.types.repository
    import aws_sdk_amplify.types.repository_clone_method
    import aws_sdk_amplify.types.service_role_arn
    import aws_sdk_amplify.types.tag_map
    import aws_sdk_amplify.types.update_time
    import aws_sdk_amplify.types.waf_configuration
    import aws_sdk_amplify.types.webhook_create_time


class App(TypedDict):
    app_id: "aws_sdk_amplify.types.app_id.AppId"
    """<p>The unique ID of the Amplify app. </p>"""
    app_arn: "aws_sdk_amplify.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the Amplify app. </p>"""
    name: "aws_sdk_amplify.types.name.Name"
    """<p>The name for the Amplify app. </p>"""
    tags: NotRequired["aws_sdk_amplify.types.tag_map.TagMap"]
    """<p>The tag for the Amplify app. </p>"""
    description: "aws_sdk_amplify.types.description.Description"
    """<p>The description for the Amplify app. </p>"""
    repository: "aws_sdk_amplify.types.repository.Repository"
    """<p>The Git repository for the Amplify app. </p>"""
    platform: "aws_sdk_amplify.types.platform.Platform"
    """<p>The platform for the Amplify app. For a static app, set the platform type to <code>WEB</code>. For a dynamic server-side rendered (SSR) app, set the platform type to <code>WEB_COMPUTE</code>. For an app requiring Amplify Hosting's original SSR support only, set the platform type to <code>WEB_DYNAMIC</code>.</p> <p>If you are deploying an SSG only app with Next.js 14 or later, you must use the platform type <code>WEB_COMPUTE</code>.</p>"""
    create_time: "aws_sdk_amplify.types.create_time.CreateTime"
    """<p>A timestamp of when Amplify created the application.</p>"""
    update_time: "aws_sdk_amplify.types.update_time.UpdateTime"
    """<p>A timestamp of when Amplify updated the application.</p>"""
    compute_role_arn: NotRequired[
        "aws_sdk_amplify.types.compute_role_arn.ComputeRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role for an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html\">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>"""
    iam_service_role_arn: NotRequired[
        "aws_sdk_amplify.types.service_role_arn.ServiceRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.</p>"""
    environment_variables: (
        "aws_sdk_amplify.types.environment_variables.EnvironmentVariables"
    )
    """<p>The environment variables for the Amplify app. </p> <p>For a list of the environment variables that are accessible to Amplify by default, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html\">Amplify Environment variables</a> in the <i>Amplify Hosting User Guide</i>.</p>"""
    default_domain: "aws_sdk_amplify.types.default_domain.DefaultDomain"
    """<p>The default domain for the Amplify app. </p>"""
    enable_branch_auto_build: (
        "aws_sdk_amplify.types.enable_branch_auto_build.EnableBranchAutoBuild"
    )
    """<p>Enables the auto-building of branches for the Amplify app. </p>"""
    enable_branch_auto_deletion: NotRequired[
        "aws_sdk_amplify.types.enable_branch_auto_deletion.EnableBranchAutoDeletion"
    ]
    """<p>Automatically disconnect a branch in the Amplify console when you delete a branch from your Git repository.</p>"""
    enable_basic_auth: "aws_sdk_amplify.types.enable_basic_auth.EnableBasicAuth"
    """<p>Enables basic authorization for the Amplify app's branches. </p>"""
    basic_auth_credentials: NotRequired[
        "aws_sdk_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p>The basic authorization credentials for branches for the Amplify app. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    custom_rules: NotRequired["aws_sdk_amplify.types.custom_rules.CustomRules"]
    """<p>Describes the custom redirect and rewrite rules for the Amplify app. </p>"""
    production_branch: NotRequired[
        "aws_sdk_amplify.types.production_branch.ProductionBranch"
    ]
    """<p>Describes the information about a production branch of the Amplify app. </p>"""
    build_spec: NotRequired["aws_sdk_amplify.types.build_spec.BuildSpec"]
    """<p>Describes the content of the build specification (build spec) for the Amplify app. </p>"""
    custom_headers: NotRequired["aws_sdk_amplify.types.custom_headers.CustomHeaders"]
    """<p>Describes the custom HTTP headers for the Amplify app.</p>"""
    enable_auto_branch_creation: NotRequired[
        "aws_sdk_amplify.types.enable_auto_branch_creation.EnableAutoBranchCreation"
    ]
    """<p>Enables automated branch creation for the Amplify app. </p>"""
    auto_branch_creation_patterns: NotRequired[
        "aws_sdk_amplify.types.auto_branch_creation_patterns.AutoBranchCreationPatterns"
    ]
    """<p>Describes the automated branch creation glob patterns for the Amplify app. </p>"""
    auto_branch_creation_config: NotRequired[
        "aws_sdk_amplify.types.auto_branch_creation_config.AutoBranchCreationConfig"
    ]
    """<p>Describes the automated branch creation configuration for the Amplify app. </p>"""
    repository_clone_method: NotRequired[
        "aws_sdk_amplify.types.repository_clone_method.RepositoryCloneMethod"
    ]
    """<note> <p>This is for internal use.</p> </note> <p>The Amplify service uses this parameter to specify the authentication protocol to use to access the Git repository for an Amplify app. Amplify specifies <code>TOKEN</code> for a GitHub repository, <code>SIGV4</code> for an Amazon Web Services CodeCommit repository, and <code>SSH</code> for GitLab and Bitbucket repositories.</p>"""
    cache_config: NotRequired["aws_sdk_amplify.types.cache_config.CacheConfig"]
    """<p>The cache configuration for the Amplify app. If you don't specify the cache configuration <code>type</code>, Amplify uses the default <code>AMPLIFY_MANAGED</code> setting.</p>"""
    webhook_create_time: NotRequired[
        "aws_sdk_amplify.types.webhook_create_time.webhookCreateTime"
    ]
    """<p>A timestamp of when Amplify created the webhook in your Git repository.</p>"""
    waf_configuration: NotRequired[
        "aws_sdk_amplify.types.waf_configuration.WafConfiguration"
    ]
    """<p>Describes the Firewall configuration for the Amplify app. Firewall support enables you to protect your hosted applications with a direct integration with WAF.</p>"""
    job_config: NotRequired["aws_sdk_amplify.types.job_config.JobConfig"]
    """<p>The configuration details that apply to the jobs for an Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: App) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_amplify.types.tag_map

        out["tags"] = aws_sdk_amplify.types.tag_map.serialize_json(value["tags"])
    out["description"] = value["description"]
    out["repository"] = value["repository"]
    import aws_sdk_amplify.types.platform

    out["platform"] = aws_sdk_amplify.types.platform.serialize_json(value["platform"])
    import aws_sdk_amplify.types.create_time

    out["createTime"] = aws_sdk_amplify.types.create_time.serialize_json(
        value["create_time"]
    )
    import aws_sdk_amplify.types.update_time

    out["updateTime"] = aws_sdk_amplify.types.update_time.serialize_json(
        value["update_time"]
    )
    if "compute_role_arn" in value:
        out["computeRoleArn"] = value["compute_role_arn"]
    if "iam_service_role_arn" in value:
        out["iamServiceRoleArn"] = value["iam_service_role_arn"]
    import aws_sdk_amplify.types.environment_variables

    out["environmentVariables"] = (
        aws_sdk_amplify.types.environment_variables.serialize_json(
            value["environment_variables"]
        )
    )
    out["defaultDomain"] = value["default_domain"]
    out["enableBranchAutoBuild"] = value["enable_branch_auto_build"]
    if "enable_branch_auto_deletion" in value:
        out["enableBranchAutoDeletion"] = value["enable_branch_auto_deletion"]
    out["enableBasicAuth"] = value["enable_basic_auth"]
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "custom_rules" in value:
        import aws_sdk_amplify.types.custom_rules

        out["customRules"] = aws_sdk_amplify.types.custom_rules.serialize_json(
            value["custom_rules"]
        )
    if "production_branch" in value:
        import aws_sdk_amplify.types.production_branch

        out["productionBranch"] = (
            aws_sdk_amplify.types.production_branch.serialize_json(
                value["production_branch"]
            )
        )
    if "build_spec" in value:
        out["buildSpec"] = value["build_spec"]
    if "custom_headers" in value:
        out["customHeaders"] = value["custom_headers"]
    if "enable_auto_branch_creation" in value:
        out["enableAutoBranchCreation"] = value["enable_auto_branch_creation"]
    if "auto_branch_creation_patterns" in value:
        import aws_sdk_amplify.types.auto_branch_creation_patterns

        out["autoBranchCreationPatterns"] = (
            aws_sdk_amplify.types.auto_branch_creation_patterns.serialize_json(
                value["auto_branch_creation_patterns"]
            )
        )
    if "auto_branch_creation_config" in value:
        import aws_sdk_amplify.types.auto_branch_creation_config

        out["autoBranchCreationConfig"] = (
            aws_sdk_amplify.types.auto_branch_creation_config.serialize_json(
                value["auto_branch_creation_config"]
            )
        )
    if "repository_clone_method" in value:
        import aws_sdk_amplify.types.repository_clone_method

        out["repositoryCloneMethod"] = (
            aws_sdk_amplify.types.repository_clone_method.serialize_json(
                value["repository_clone_method"]
            )
        )
    if "cache_config" in value:
        import aws_sdk_amplify.types.cache_config

        out["cacheConfig"] = aws_sdk_amplify.types.cache_config.serialize_json(
            value["cache_config"]
        )
    if "webhook_create_time" in value:
        import aws_sdk_amplify.types.webhook_create_time

        out["webhookCreateTime"] = (
            aws_sdk_amplify.types.webhook_create_time.serialize_json(
                value["webhook_create_time"]
            )
        )
    if "waf_configuration" in value:
        import aws_sdk_amplify.types.waf_configuration

        out["wafConfiguration"] = (
            aws_sdk_amplify.types.waf_configuration.serialize_json(
                value["waf_configuration"]
            )
        )
    if "job_config" in value:
        import aws_sdk_amplify.types.job_config

        out["jobConfig"] = aws_sdk_amplify.types.job_config.serialize_json(
            value["job_config"]
        )
    return out


def deserialize_json(data: dict) -> App:
    out: App = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("App.app_id required")
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("App.app_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("App.name required")
    if "tags" in data:
        import aws_sdk_amplify.types.tag_map

        out["tags"] = aws_sdk_amplify.types.tag_map.deserialize_json(data["tags"])
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("App.description required")
    if "repository" in data:
        out["repository"] = data["repository"]
    else:
        raise DeserializationError("App.repository required")
    if "platform" in data:
        import aws_sdk_amplify.types.platform

        out["platform"] = aws_sdk_amplify.types.platform.deserialize_json(
            data["platform"]
        )
    else:
        raise DeserializationError("App.platform required")
    if "createTime" in data:
        import aws_sdk_amplify.types.create_time

        out["create_time"] = aws_sdk_amplify.types.create_time.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("App.create_time required")
    if "updateTime" in data:
        import aws_sdk_amplify.types.update_time

        out["update_time"] = aws_sdk_amplify.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("App.update_time required")
    if "computeRoleArn" in data:
        out["compute_role_arn"] = data["computeRoleArn"]
    if "iamServiceRoleArn" in data:
        out["iam_service_role_arn"] = data["iamServiceRoleArn"]
    if "environmentVariables" in data:
        import aws_sdk_amplify.types.environment_variables

        out["environment_variables"] = (
            aws_sdk_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    else:
        raise DeserializationError("App.environment_variables required")
    if "defaultDomain" in data:
        out["default_domain"] = data["defaultDomain"]
    else:
        raise DeserializationError("App.default_domain required")
    if "enableBranchAutoBuild" in data:
        out["enable_branch_auto_build"] = data["enableBranchAutoBuild"]
    else:
        raise DeserializationError("App.enable_branch_auto_build required")
    if "enableBranchAutoDeletion" in data:
        out["enable_branch_auto_deletion"] = data["enableBranchAutoDeletion"]
    if "enableBasicAuth" in data:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    else:
        raise DeserializationError("App.enable_basic_auth required")
    if "basicAuthCredentials" in data:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if "customRules" in data:
        import aws_sdk_amplify.types.custom_rules

        out["custom_rules"] = aws_sdk_amplify.types.custom_rules.deserialize_json(
            data["customRules"]
        )
    if "productionBranch" in data:
        import aws_sdk_amplify.types.production_branch

        out["production_branch"] = (
            aws_sdk_amplify.types.production_branch.deserialize_json(
                data["productionBranch"]
            )
        )
    if "buildSpec" in data:
        out["build_spec"] = data["buildSpec"]
    if "customHeaders" in data:
        out["custom_headers"] = data["customHeaders"]
    if "enableAutoBranchCreation" in data:
        out["enable_auto_branch_creation"] = data["enableAutoBranchCreation"]
    if "autoBranchCreationPatterns" in data:
        import aws_sdk_amplify.types.auto_branch_creation_patterns

        out["auto_branch_creation_patterns"] = (
            aws_sdk_amplify.types.auto_branch_creation_patterns.deserialize_json(
                data["autoBranchCreationPatterns"]
            )
        )
    if "autoBranchCreationConfig" in data:
        import aws_sdk_amplify.types.auto_branch_creation_config

        out["auto_branch_creation_config"] = (
            aws_sdk_amplify.types.auto_branch_creation_config.deserialize_json(
                data["autoBranchCreationConfig"]
            )
        )
    if "repositoryCloneMethod" in data:
        import aws_sdk_amplify.types.repository_clone_method

        out["repository_clone_method"] = (
            aws_sdk_amplify.types.repository_clone_method.deserialize_json(
                data["repositoryCloneMethod"]
            )
        )
    if "cacheConfig" in data:
        import aws_sdk_amplify.types.cache_config

        out["cache_config"] = aws_sdk_amplify.types.cache_config.deserialize_json(
            data["cacheConfig"]
        )
    if "webhookCreateTime" in data:
        import aws_sdk_amplify.types.webhook_create_time

        out["webhook_create_time"] = (
            aws_sdk_amplify.types.webhook_create_time.deserialize_json(
                data["webhookCreateTime"]
            )
        )
    if "wafConfiguration" in data:
        import aws_sdk_amplify.types.waf_configuration

        out["waf_configuration"] = (
            aws_sdk_amplify.types.waf_configuration.deserialize_json(
                data["wafConfiguration"]
            )
        )
    if "jobConfig" in data:
        import aws_sdk_amplify.types.job_config

        out["job_config"] = aws_sdk_amplify.types.job_config.deserialize_json(
            data["jobConfig"]
        )
    return out
