"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.content_source_configuration
    import capo_kendra.types.user_identity_configuration


class ExperienceConfiguration(TypedDict, closed=True):
    content_source_configuration: NotRequired[
        "capo_kendra.types.content_source_configuration.ContentSourceConfiguration"
    ]
    """<p>The identifiers of your data sources and FAQs. Or, you can specify that you want to use documents indexed via the <code>BatchPutDocument</code> API. This is the content you want to use for your Amazon Kendra experience.</p>"""
    user_identity_configuration: NotRequired[
        "capo_kendra.types.user_identity_configuration.UserIdentityConfiguration"
    ]
    """<p>The IAM Identity Center field name that contains the identifiers of your users, such as their emails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceConfiguration) -> dict:
    out: dict = {}
    if "content_source_configuration" in value:
        import capo_kendra.types.content_source_configuration

        out["ContentSourceConfiguration"] = (
            capo_kendra.types.content_source_configuration.serialize_aws_json_1_1(
                value["content_source_configuration"]
            )
        )
    if "user_identity_configuration" in value:
        import capo_kendra.types.user_identity_configuration

        out["UserIdentityConfiguration"] = (
            capo_kendra.types.user_identity_configuration.serialize_aws_json_1_1(
                value["user_identity_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperienceConfiguration:
    out: ExperienceConfiguration = {}  # type: ignore[typeddict-item]
    if "ContentSourceConfiguration" in data:
        import capo_kendra.types.content_source_configuration

        out["content_source_configuration"] = (
            capo_kendra.types.content_source_configuration.deserialize_aws_json_1_1(
                data["ContentSourceConfiguration"]
            )
        )
    if "UserIdentityConfiguration" in data:
        import capo_kendra.types.user_identity_configuration

        out["user_identity_configuration"] = (
            capo_kendra.types.user_identity_configuration.deserialize_aws_json_1_1(
                data["UserIdentityConfiguration"]
            )
        )
    return out
