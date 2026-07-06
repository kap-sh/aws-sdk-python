"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ConflictResolution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.conflict_resolving_model
    import aws_sdk_customer_profiles.types.string1_to255


class ConflictResolution(TypedDict, closed=True):
    conflict_resolving_model: "aws_sdk_customer_profiles.types.conflict_resolving_model.ConflictResolvingModel"
    """<p>How the auto-merging process should resolve conflicts between different profiles.</p> <ul> <li> <p> <code>RECENCY</code>: Uses the data that was most recently updated.</p> </li> <li> <p> <code>SOURCE</code>: Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then <code>RECENCY</code> is used again.</p> </li> </ul>"""
    source_name: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The <code>ObjectType</code> name that is used to resolve profile merging conflicts when choosing <code>SOURCE</code> as the <code>ConflictResolvingModel</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictResolution) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.conflict_resolving_model

    out["ConflictResolvingModel"] = (
        aws_sdk_customer_profiles.types.conflict_resolving_model.serialize_json(
            value["conflict_resolving_model"]
        )
    )
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    return out


def deserialize_json(data: dict) -> ConflictResolution:
    out: ConflictResolution = {}  # type: ignore[typeddict-item]
    if "ConflictResolvingModel" in data:
        import aws_sdk_customer_profiles.types.conflict_resolving_model

        out["conflict_resolving_model"] = (
            aws_sdk_customer_profiles.types.conflict_resolving_model.deserialize_json(
                data["ConflictResolvingModel"]
            )
        )
    else:
        raise DeserializationError(
            "ConflictResolution.conflict_resolving_model required"
        )
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    return out
