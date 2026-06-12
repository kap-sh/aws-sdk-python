"""Generated from Smithy shape ``com.amazonaws.iot#DeleteThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.thing_name


class DeleteThingRequest(TypedDict):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing to delete.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the <code>DeleteThing</code> request is rejected with a <code>VersionConflictException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThingRequest:
    out: DeleteThingRequest = {}  # type: ignore[typeddict-item]
    return out
