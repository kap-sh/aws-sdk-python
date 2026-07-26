"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateRetrievalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string_min1_max64_pattern_w
    import capo_macie2.types.retrieval_mode


class UpdateRetrievalConfiguration(TypedDict, closed=True):
    retrieval_mode: NotRequired["capo_macie2.types.retrieval_mode.RetrievalMode"]
    """<p>The access method to use when retrieving sensitive data from affected S3 objects. Valid values are: ASSUME_ROLE, assume an IAM role that is in the affected Amazon Web Services account and delegates access to Amazon Macie; and, CALLER_CREDENTIALS, use the credentials of the IAM user who requests the sensitive data. If you specify ASSUME_ROLE, also specify the name of an existing IAM role for Macie to assume (roleName).</p> <important><p>If you change this value from ASSUME_ROLE to CALLER_CREDENTIALS for an existing configuration, Macie permanently deletes the external ID and role name currently specified for the configuration. These settings can't be recovered after they're deleted.</p></important>"""
    role_name: NotRequired[
        "capo_macie2.types.__string_min1_max64_pattern_w.__stringMin1Max64PatternW"
    ]
    """<p>The name of the IAM role that is in the affected Amazon Web Services account and Amazon Macie is allowed to assume when retrieving sensitive data from affected S3 objects for the account. The trust and permissions policies for the role must meet all requirements for Macie to assume the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRetrievalConfiguration) -> dict:
    out: dict = {}
    if "retrieval_mode" in value:
        import capo_macie2.types.retrieval_mode

        out["retrievalMode"] = capo_macie2.types.retrieval_mode.serialize_json(
            value["retrieval_mode"]
        )
    if "role_name" in value:
        out["roleName"] = value["role_name"]
    return out


def deserialize_json(data: dict) -> UpdateRetrievalConfiguration:
    out: UpdateRetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if "retrievalMode" in data:
        import capo_macie2.types.retrieval_mode

        out["retrieval_mode"] = capo_macie2.types.retrieval_mode.deserialize_json(
            data["retrievalMode"]
        )
    if "roleName" in data:
        out["role_name"] = data["roleName"]
    return out
