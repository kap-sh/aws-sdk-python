"""Generated from Smithy shape ``com.amazonaws.odb#ListSystemVersionsInput``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError


class ListSystemVersionsInput(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    gi_version: "str"
    """<p>The software version of the Exadata Grid Infrastructure (GI).</p>"""
    shape: "str"
    """<p>The Exadata hardware system model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSystemVersionsInput) -> dict:
    out: dict = {}
    out["giVersion"] = value["gi_version"]
    out["shape"] = value["shape"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSystemVersionsInput:
    out: ListSystemVersionsInput = {}  # type: ignore[typeddict-item]
    if "giVersion" in data:
        out["gi_version"] = data["giVersion"]
    else:
        raise DeserializationError("ListSystemVersionsInput.gi_version required")
    if "shape" in data:
        out["shape"] = data["shape"]
    else:
        raise DeserializationError("ListSystemVersionsInput.shape required")
    return out
