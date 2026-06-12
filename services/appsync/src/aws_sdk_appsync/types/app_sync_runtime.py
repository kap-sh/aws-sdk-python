"""Generated from Smithy shape ``com.amazonaws.appsync#AppSyncRuntime``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.runtime_name
    import aws_sdk_appsync.types.string


class AppSyncRuntime(TypedDict):
    name: "aws_sdk_appsync.types.runtime_name.RuntimeName"
    """<p>The <code>name</code> of the runtime to use. Currently, the only allowed value is <code>APPSYNC_JS</code>.</p>"""
    runtime_version: "aws_sdk_appsync.types.string.String"
    """<p>The <code>version</code> of the runtime to use. Currently, the only allowed version is <code>1.0.0</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppSyncRuntime) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.runtime_name

    out["name"] = aws_sdk_appsync.types.runtime_name.serialize_json(value["name"])
    out["runtimeVersion"] = value["runtime_version"]
    return out


def deserialize_json(data: dict) -> AppSyncRuntime:
    out: AppSyncRuntime = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_appsync.types.runtime_name

        out["name"] = aws_sdk_appsync.types.runtime_name.deserialize_json(data["name"])
    else:
        raise DeserializationError("AppSyncRuntime.name required")
    if "runtimeVersion" in data:
        out["runtime_version"] = data["runtimeVersion"]
    else:
        raise DeserializationError("AppSyncRuntime.runtime_version required")
    return out
