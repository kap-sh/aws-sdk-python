"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetWebExperienceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.browser_extension_configuration
    import capo_qbusiness.types.customization_configuration
    import capo_qbusiness.types.error_detail
    import capo_qbusiness.types.identity_provider_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.timestamp
    import capo_qbusiness.types.url
    import capo_qbusiness.types.web_experience_arn
    import capo_qbusiness.types.web_experience_auth_configuration
    import capo_qbusiness.types.web_experience_id
    import capo_qbusiness.types.web_experience_origins
    import capo_qbusiness.types.web_experience_sample_prompts_control_mode
    import capo_qbusiness.types.web_experience_status
    import capo_qbusiness.types.web_experience_subtitle
    import capo_qbusiness.types.web_experience_title
    import capo_qbusiness.types.web_experience_welcome_message


class GetWebExperienceResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application linked to the web experience.</p>"""
    web_experience_id: NotRequired[
        "capo_qbusiness.types.web_experience_id.WebExperienceId"
    ]
    """<p>The identifier of the Amazon Q Business web experience.</p>"""
    web_experience_arn: NotRequired[
        "capo_qbusiness.types.web_experience_arn.WebExperienceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the role with the permission to access the Amazon Q Business web experience and required resources.</p>"""
    default_endpoint: NotRequired["capo_qbusiness.types.url.Url"]
    """<p>The endpoint of your Amazon Q Business web experience.</p>"""
    status: NotRequired[
        "capo_qbusiness.types.web_experience_status.WebExperienceStatus"
    ]
    """<p>The current status of the Amazon Q Business web experience. When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the data source connector to fail. </p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business web experience was last created.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business web experience was last updated.</p>"""
    title: NotRequired["capo_qbusiness.types.web_experience_title.WebExperienceTitle"]
    """<p>The title for your Amazon Q Business web experience. </p>"""
    subtitle: NotRequired[
        "capo_qbusiness.types.web_experience_subtitle.WebExperienceSubtitle"
    ]
    """<p>The subtitle for your Amazon Q Business web experience. </p>"""
    welcome_message: NotRequired[
        "capo_qbusiness.types.web_experience_welcome_message.WebExperienceWelcomeMessage"
    ]
    """<p>The customized welcome message for end users of an Amazon Q Business web experience.</p>"""
    sample_prompts_control_mode: NotRequired[
        "capo_qbusiness.types.web_experience_sample_prompts_control_mode.WebExperienceSamplePromptsControlMode"
    ]
    """<p>Determines whether sample prompts are enabled in the web experience for an end user.</p>"""
    origins: NotRequired[
        "capo_qbusiness.types.web_experience_origins.WebExperienceOrigins"
    ]
    """<p>Gets the website domain origins that are allowed to embed the Amazon Q Business web experience. The <i>domain origin</i> refers to the base URL for accessing a website including the protocol (<code>http/https</code>), the domain name, and the port number (if specified). </p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p> The Amazon Resource Name (ARN) of the service role attached to your web experience.</p>"""
    identity_provider_configuration: NotRequired[
        "capo_qbusiness.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.</p>"""
    authentication_configuration: NotRequired[
        "capo_qbusiness.types.web_experience_auth_configuration.WebExperienceAuthConfiguration"
    ]
    """<p>The authentication configuration information for your Amazon Q Business web experience.</p>"""
    error: NotRequired["capo_qbusiness.types.error_detail.ErrorDetail"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a description of the error that caused the data source connector to fail.</p>"""
    browser_extension_configuration: NotRequired[
        "capo_qbusiness.types.browser_extension_configuration.BrowserExtensionConfiguration"
    ]
    """<p>The browser extension configuration for an Amazon Q Business web experience.</p>"""
    customization_configuration: NotRequired[
        "capo_qbusiness.types.customization_configuration.CustomizationConfiguration"
    ]
    """<p>Gets the custom logo, favicon, font, and color used in the Amazon Q web experience. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebExperienceResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "web_experience_id" in value:
        out["webExperienceId"] = value["web_experience_id"]
    if "web_experience_arn" in value:
        out["webExperienceArn"] = value["web_experience_arn"]
    if "default_endpoint" in value:
        out["defaultEndpoint"] = value["default_endpoint"]
    if "status" in value:
        import capo_qbusiness.types.web_experience_status

        out["status"] = capo_qbusiness.types.web_experience_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "subtitle" in value:
        out["subtitle"] = value["subtitle"]
    if "welcome_message" in value:
        out["welcomeMessage"] = value["welcome_message"]
    if "sample_prompts_control_mode" in value:
        import capo_qbusiness.types.web_experience_sample_prompts_control_mode

        out["samplePromptsControlMode"] = (
            capo_qbusiness.types.web_experience_sample_prompts_control_mode.serialize_json(
                value["sample_prompts_control_mode"]
            )
        )
    if "origins" in value:
        import capo_qbusiness.types.web_experience_origins

        out["origins"] = capo_qbusiness.types.web_experience_origins.serialize_json(
            value["origins"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "identity_provider_configuration" in value:
        import capo_qbusiness.types.identity_provider_configuration

        out["identityProviderConfiguration"] = (
            capo_qbusiness.types.identity_provider_configuration.serialize_json(
                value["identity_provider_configuration"]
            )
        )
    if "authentication_configuration" in value:
        import capo_qbusiness.types.web_experience_auth_configuration

        out["authenticationConfiguration"] = (
            capo_qbusiness.types.web_experience_auth_configuration.serialize_json(
                value["authentication_configuration"]
            )
        )
    if "error" in value:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.serialize_json(value["error"])
    if "browser_extension_configuration" in value:
        import capo_qbusiness.types.browser_extension_configuration

        out["browserExtensionConfiguration"] = (
            capo_qbusiness.types.browser_extension_configuration.serialize_json(
                value["browser_extension_configuration"]
            )
        )
    if "customization_configuration" in value:
        import capo_qbusiness.types.customization_configuration

        out["customizationConfiguration"] = (
            capo_qbusiness.types.customization_configuration.serialize_json(
                value["customization_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWebExperienceResponse:
    out: GetWebExperienceResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "webExperienceId" in data:
        out["web_experience_id"] = data["webExperienceId"]
    if "webExperienceArn" in data:
        out["web_experience_arn"] = data["webExperienceArn"]
    if "defaultEndpoint" in data:
        out["default_endpoint"] = data["defaultEndpoint"]
    if "status" in data:
        import capo_qbusiness.types.web_experience_status

        out["status"] = capo_qbusiness.types.web_experience_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "title" in data:
        out["title"] = data["title"]
    if "subtitle" in data:
        out["subtitle"] = data["subtitle"]
    if "welcomeMessage" in data:
        out["welcome_message"] = data["welcomeMessage"]
    if "samplePromptsControlMode" in data:
        import capo_qbusiness.types.web_experience_sample_prompts_control_mode

        out["sample_prompts_control_mode"] = (
            capo_qbusiness.types.web_experience_sample_prompts_control_mode.deserialize_json(
                data["samplePromptsControlMode"]
            )
        )
    if "origins" in data:
        import capo_qbusiness.types.web_experience_origins

        out["origins"] = capo_qbusiness.types.web_experience_origins.deserialize_json(
            data["origins"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "identityProviderConfiguration" in data:
        import capo_qbusiness.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_qbusiness.types.identity_provider_configuration.deserialize_json(
                data["identityProviderConfiguration"]
            )
        )
    if "authenticationConfiguration" in data:
        import capo_qbusiness.types.web_experience_auth_configuration

        out["authentication_configuration"] = (
            capo_qbusiness.types.web_experience_auth_configuration.deserialize_json(
                data["authenticationConfiguration"]
            )
        )
    if "error" in data:
        import capo_qbusiness.types.error_detail

        out["error"] = capo_qbusiness.types.error_detail.deserialize_json(data["error"])
    if "browserExtensionConfiguration" in data:
        import capo_qbusiness.types.browser_extension_configuration

        out["browser_extension_configuration"] = (
            capo_qbusiness.types.browser_extension_configuration.deserialize_json(
                data["browserExtensionConfiguration"]
            )
        )
    if "customizationConfiguration" in data:
        import capo_qbusiness.types.customization_configuration

        out["customization_configuration"] = (
            capo_qbusiness.types.customization_configuration.deserialize_json(
                data["customizationConfiguration"]
            )
        )
    return out
