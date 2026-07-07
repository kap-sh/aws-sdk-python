"""Generated from Smithy shape ``com.amazonaws.sagemaker#TotalHits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.long
    import aws_sdk_sagemaker.types.relation


class TotalHits(TypedDict, closed=True):
    value: NotRequired["aws_sdk_sagemaker.types.long.Long"]
    """<p>The total number of matching results. This value may be exact or an estimate, depending on the <code>Relation</code> field.</p>"""
    relation: NotRequired["aws_sdk_sagemaker.types.relation.Relation"]
    """<p>Indicates the relationship between the returned <code>Value</code> and the actual total number of matching results. Possible values are:</p> <ul> <li> <p> <code>EqualTo</code>: The <code>Value</code> is the exact count of matching results.</p> </li> <li> <p> <code>GreaterThanOrEqualTo</code>: The <code>Value</code> is a lower bound of the actual count of matching results.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TotalHits) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "relation" in value:
        import aws_sdk_sagemaker.types.relation

        out["Relation"] = aws_sdk_sagemaker.types.relation.serialize_aws_json_1_1(
            value["relation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TotalHits:
    out: TotalHits = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Relation" in data:
        import aws_sdk_sagemaker.types.relation

        out["relation"] = aws_sdk_sagemaker.types.relation.deserialize_aws_json_1_1(
            data["Relation"]
        )
    return out
