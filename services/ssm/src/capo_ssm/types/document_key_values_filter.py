"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentKeyValuesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_key_values_filter_key
    import capo_ssm.types.document_key_values_filter_values


class DocumentKeyValuesFilter(TypedDict, closed=True):
    key: NotRequired[
        "capo_ssm.types.document_key_values_filter_key.DocumentKeyValuesFilterKey"
    ]
    """<p>The name of the filter key.</p>"""
    values: NotRequired[
        "capo_ssm.types.document_key_values_filter_values.DocumentKeyValuesFilterValues"
    ]
    """<p>The value for the filter key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentKeyValuesFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_ssm.types.document_key_values_filter_values

        out["Values"] = (
            capo_ssm.types.document_key_values_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentKeyValuesFilter:
    out: DocumentKeyValuesFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import capo_ssm.types.document_key_values_filter_values

        out["values"] = (
            capo_ssm.types.document_key_values_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
