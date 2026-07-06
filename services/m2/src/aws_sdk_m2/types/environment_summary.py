"""Generated from Smithy shape ``com.amazonaws.m2#EnvironmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.arn
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.engine_version
    import aws_sdk_m2.types.entity_name
    import aws_sdk_m2.types.environment_lifecycle
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.network_type
    import aws_sdk_m2.types.string20
    import aws_sdk_m2.types.timestamp


class EnvironmentSummary(TypedDict, closed=True):
    name: "aws_sdk_m2.types.entity_name.EntityName"
    """<p>The name of the runtime environment.</p>"""
    environment_arn: "aws_sdk_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of a particular runtime environment.</p>"""
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of a particular runtime environment.</p>"""
    instance_type: "aws_sdk_m2.types.string20.String20"
    """<p>The instance type of the runtime environment.</p>"""
    status: "aws_sdk_m2.types.environment_lifecycle.EnvironmentLifecycle"
    """<p>The status of the runtime environment</p>"""
    engine_type: "aws_sdk_m2.types.engine_type.EngineType"
    """<p>The target platform for the runtime environment.</p>"""
    engine_version: "aws_sdk_m2.types.engine_version.EngineVersion"
    """<p>The version of the runtime engine.</p>"""
    creation_time: "aws_sdk_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the runtime environment was created.</p>"""
    network_type: NotRequired["aws_sdk_m2.types.network_type.NetworkType"]
    """<p>The network type supported by the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["environmentArn"] = value["environment_arn"]
    out["environmentId"] = value["environment_id"]
    out["instanceType"] = value["instance_type"]
    out["status"] = value["status"]
    out["engineType"] = value["engine_type"]
    out["engineVersion"] = value["engine_version"]
    import aws_sdk_m2.types.timestamp

    out["creationTime"] = aws_sdk_m2.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    return out


def deserialize_json(data: dict) -> EnvironmentSummary:
    out: EnvironmentSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EnvironmentSummary.name required")
    if "environmentArn" in data:
        out["environment_arn"] = data["environmentArn"]
    else:
        raise DeserializationError("EnvironmentSummary.environment_arn required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("EnvironmentSummary.environment_id required")
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("EnvironmentSummary.instance_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("EnvironmentSummary.status required")
    if "engineType" in data:
        out["engine_type"] = data["engineType"]
    else:
        raise DeserializationError("EnvironmentSummary.engine_type required")
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    else:
        raise DeserializationError("EnvironmentSummary.engine_version required")
    if "creationTime" in data:
        import aws_sdk_m2.types.timestamp

        out["creation_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("EnvironmentSummary.creation_time required")
    if "networkType" in data:
        out["network_type"] = data["networkType"]
    return out
