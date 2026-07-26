"""Generated from Smithy shape ``com.amazonaws.codecommit#IsBinaryFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.capital_boolean


class IsBinaryFile(TypedDict, closed=True):
    source: NotRequired["capo_codecommit.types.capital_boolean.CapitalBoolean"]
    """<p>The binary or non-binary status of file in the source of a merge or pull request.</p>"""
    destination: NotRequired["capo_codecommit.types.capital_boolean.CapitalBoolean"]
    """<p>The binary or non-binary status of a file in the destination of a merge or pull request.</p>"""
    base: NotRequired["capo_codecommit.types.capital_boolean.CapitalBoolean"]
    """<p>The binary or non-binary status of a file in the base of a merge or pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsBinaryFile) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    if "destination" in value:
        out["destination"] = value["destination"]
    if "base" in value:
        out["base"] = value["base"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IsBinaryFile:
    out: IsBinaryFile = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "destination" in data:
        out["destination"] = data["destination"]
    if "base" in data:
        out["base"] = data["base"]
    return out
