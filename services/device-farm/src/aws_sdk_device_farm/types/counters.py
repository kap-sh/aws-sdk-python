"""Generated from Smithy shape ``com.amazonaws.devicefarm#Counters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.integer


class Counters(TypedDict, closed=True):
    total: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The total number of entities.</p>"""
    passed: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of passed entities.</p>"""
    failed: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of failed entities.</p>"""
    warned: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of warned entities.</p>"""
    errored: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of errored entities.</p>"""
    stopped: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of stopped entities.</p>"""
    skipped: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of skipped entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Counters) -> dict:
    out: dict = {}
    if "total" in value:
        out["total"] = value["total"]
    if "passed" in value:
        out["passed"] = value["passed"]
    if "failed" in value:
        out["failed"] = value["failed"]
    if "warned" in value:
        out["warned"] = value["warned"]
    if "errored" in value:
        out["errored"] = value["errored"]
    if "stopped" in value:
        out["stopped"] = value["stopped"]
    if "skipped" in value:
        out["skipped"] = value["skipped"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Counters:
    out: Counters = {}  # type: ignore[typeddict-item]
    if "total" in data:
        out["total"] = data["total"]
    if "passed" in data:
        out["passed"] = data["passed"]
    if "failed" in data:
        out["failed"] = data["failed"]
    if "warned" in data:
        out["warned"] = data["warned"]
    if "errored" in data:
        out["errored"] = data["errored"]
    if "stopped" in data:
        out["stopped"] = data["stopped"]
    if "skipped" in data:
        out["skipped"] = data["skipped"]
    return out
