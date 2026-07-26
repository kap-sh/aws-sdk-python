"""Generated from Smithy shape ``com.amazonaws.quicksight#GenerateEmbedUrlForRegisteredUserWithIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.registered_user_embedding_experience_configuration
    import capo_quicksight.types.session_lifetime_in_minutes
    import capo_quicksight.types.string_list


class GenerateEmbedUrlForRegisteredUserWithIdentityRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services registered user.</p>"""
    session_lifetime_in_minutes: NotRequired[
        "capo_quicksight.types.session_lifetime_in_minutes.SessionLifetimeInMinutes"
    ]
    """<p>The validity of the session in minutes.</p>"""
    experience_configuration: "capo_quicksight.types.registered_user_embedding_experience_configuration.RegisteredUserEmbeddingExperienceConfiguration"
    allowed_domains: NotRequired["capo_quicksight.types.string_list.StringList"]
    """<p>A list of domains to be allowed to generate the embed URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateEmbedUrlForRegisteredUserWithIdentityRequest) -> dict:
    out: dict = {}
    if "session_lifetime_in_minutes" in value:
        out["SessionLifetimeInMinutes"] = value["session_lifetime_in_minutes"]
    import capo_quicksight.types.registered_user_embedding_experience_configuration

    out["ExperienceConfiguration"] = (
        capo_quicksight.types.registered_user_embedding_experience_configuration.serialize_json(
            value["experience_configuration"]
        )
    )
    if "allowed_domains" in value:
        import capo_quicksight.types.string_list

        out["AllowedDomains"] = capo_quicksight.types.string_list.serialize_json(
            value["allowed_domains"]
        )
    return out


def deserialize_json(
    data: dict,
) -> GenerateEmbedUrlForRegisteredUserWithIdentityRequest:
    out: GenerateEmbedUrlForRegisteredUserWithIdentityRequest = {}  # type: ignore[typeddict-item]
    if "SessionLifetimeInMinutes" in data:
        out["session_lifetime_in_minutes"] = data["SessionLifetimeInMinutes"]
    if "ExperienceConfiguration" in data:
        import capo_quicksight.types.registered_user_embedding_experience_configuration

        out["experience_configuration"] = (
            capo_quicksight.types.registered_user_embedding_experience_configuration.deserialize_json(
                data["ExperienceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateEmbedUrlForRegisteredUserWithIdentityRequest.experience_configuration required"
        )
    if "AllowedDomains" in data:
        import capo_quicksight.types.string_list

        out["allowed_domains"] = capo_quicksight.types.string_list.deserialize_json(
            data["AllowedDomains"]
        )
    return out
