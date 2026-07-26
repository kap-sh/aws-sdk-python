"""Generated from Smithy shape ``com.amazonaws.macie2#RetrievalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.__string_min1_max64_pattern_w
    import capo_macie2.types.retrieval_mode


class RetrievalConfiguration(TypedDict, closed=True):
    external_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The external ID to specify in the trust policy for the IAM role to assume when retrieving sensitive data from affected S3 objects (roleName). This value is null if the value for retrievalMode is CALLER_CREDENTIALS.</p> <p>This ID is a unique alphanumeric string that Amazon Macie generates automatically after you configure it to assume an IAM role. For a Macie administrator to retrieve sensitive data from an affected S3 object for a member account, the trust policy for the role in the member account must include an sts:ExternalId condition that requires this ID.</p>"""
    retrieval_mode: NotRequired["capo_macie2.types.retrieval_mode.RetrievalMode"]
    """<p>The access method that's used to retrieve sensitive data from affected S3 objects. Valid values are: ASSUME_ROLE, assume an IAM role that is in the affected Amazon Web Services account and delegates access to Amazon Macie (roleName); and, CALLER_CREDENTIALS, use the credentials of the IAM user who requests the sensitive data.</p>"""
    role_name: NotRequired[
        "capo_macie2.types.__string_min1_max64_pattern_w.__stringMin1Max64PatternW"
    ]
    """<p>The name of the IAM role that is in the affected Amazon Web Services account and Amazon Macie is allowed to assume when retrieving sensitive data from affected S3 objects for the account. This value is null if the value for retrievalMode is CALLER_CREDENTIALS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalConfiguration) -> dict:
    out: dict = {}
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "retrieval_mode" in value:
        import capo_macie2.types.retrieval_mode

        out["retrievalMode"] = capo_macie2.types.retrieval_mode.serialize_json(
            value["retrieval_mode"]
        )
    if "role_name" in value:
        out["roleName"] = value["role_name"]
    return out


def deserialize_json(data: dict) -> RetrievalConfiguration:
    out: RetrievalConfiguration = {}  # type: ignore[typeddict-item]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "retrievalMode" in data:
        import capo_macie2.types.retrieval_mode

        out["retrieval_mode"] = capo_macie2.types.retrieval_mode.deserialize_json(
            data["retrievalMode"]
        )
    if "roleName" in data:
        out["role_name"] = data["roleName"]
    return out
