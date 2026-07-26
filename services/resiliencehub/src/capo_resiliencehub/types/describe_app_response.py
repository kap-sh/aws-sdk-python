"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.app


class DescribeAppResponse(TypedDict, closed=True):
    app: "capo_resiliencehub.types.app.App"
    """<p>The specified application, returned as an object with details including compliance status, creation time, description, resiliency score, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.app

    out["app"] = capo_resiliencehub.types.app.serialize_json(value["app"])
    return out


def deserialize_json(data: dict) -> DescribeAppResponse:
    out: DescribeAppResponse = {}  # type: ignore[typeddict-item]
    if "app" in data:
        import capo_resiliencehub.types.app

        out["app"] = capo_resiliencehub.types.app.deserialize_json(data["app"])
    else:
        raise DeserializationError("DescribeAppResponse.app required")
    return out
