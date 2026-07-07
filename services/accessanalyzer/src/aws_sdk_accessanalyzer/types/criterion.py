"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Criterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.value_list


class Criterion(TypedDict, closed=True):
    eq: NotRequired["aws_sdk_accessanalyzer.types.value_list.ValueList"]
    r"""<p>An \"equals\" operator to match for the filter used to create the rule.</p>"""
    neq: NotRequired["aws_sdk_accessanalyzer.types.value_list.ValueList"]
    r"""<p>A \"not equals\" operator to match for the filter used to create the rule.</p>"""
    contains: NotRequired["aws_sdk_accessanalyzer.types.value_list.ValueList"]
    r"""<p>A \"contains\" operator to match for the filter used to create the rule.</p>"""
    exists: NotRequired["bool"]
    r"""<p>An \"exists\" operator to match for the filter used to create the rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Criterion) -> dict:
    out: dict = {}
    if "eq" in value:
        import aws_sdk_accessanalyzer.types.value_list

        out["eq"] = aws_sdk_accessanalyzer.types.value_list.serialize_json(value["eq"])
    if "neq" in value:
        import aws_sdk_accessanalyzer.types.value_list

        out["neq"] = aws_sdk_accessanalyzer.types.value_list.serialize_json(
            value["neq"]
        )
    if "contains" in value:
        import aws_sdk_accessanalyzer.types.value_list

        out["contains"] = aws_sdk_accessanalyzer.types.value_list.serialize_json(
            value["contains"]
        )
    if "exists" in value:
        out["exists"] = value["exists"]
    return out


def deserialize_json(data: dict) -> Criterion:
    out: Criterion = {}  # type: ignore[typeddict-item]
    if "eq" in data:
        import aws_sdk_accessanalyzer.types.value_list

        out["eq"] = aws_sdk_accessanalyzer.types.value_list.deserialize_json(data["eq"])
    if "neq" in data:
        import aws_sdk_accessanalyzer.types.value_list

        out["neq"] = aws_sdk_accessanalyzer.types.value_list.deserialize_json(
            data["neq"]
        )
    if "contains" in data:
        import aws_sdk_accessanalyzer.types.value_list

        out["contains"] = aws_sdk_accessanalyzer.types.value_list.deserialize_json(
            data["contains"]
        )
    if "exists" in data:
        out["exists"] = data["exists"]
    return out
