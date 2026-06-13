"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_controlcatalog.types.associated_domain_summary
    import aws_sdk_controlcatalog.types.objective_arn


class ObjectiveSummary(TypedDict):
    arn: "aws_sdk_controlcatalog.types.objective_arn.ObjectiveArn"
    """<p>The Amazon Resource Name (ARN) that identifies the objective.</p>"""
    name: "str"
    """<p>The name of the objective.</p>"""
    description: "str"
    """<p>The description of the objective.</p>"""
    domain: (
        "aws_sdk_controlcatalog.types.associated_domain_summary.AssociatedDomainSummary"
    )
    """<p>The domain that the objective belongs to.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the objective was created.</p>"""
    last_update_time: "datetime.datetime"
    """<p>The time when the objective was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import aws_sdk_controlcatalog.types.associated_domain_summary

    out["Domain"] = (
        aws_sdk_controlcatalog.types.associated_domain_summary.serialize_json(
            value["domain"]
        )
    )
    import aws_sdk_controlcatalog.types._prelude.timestamp

    out["CreateTime"] = aws_sdk_controlcatalog.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_controlcatalog.types._prelude.timestamp

    out["LastUpdateTime"] = (
        aws_sdk_controlcatalog.types._prelude.timestamp.serialize_json(
            value["last_update_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> ObjectiveSummary:
    out: ObjectiveSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ObjectiveSummary.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ObjectiveSummary.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("ObjectiveSummary.description required")
    if "Domain" in data:
        import aws_sdk_controlcatalog.types.associated_domain_summary

        out["domain"] = (
            aws_sdk_controlcatalog.types.associated_domain_summary.deserialize_json(
                data["Domain"]
            )
        )
    else:
        raise DeserializationError("ObjectiveSummary.domain required")
    if "CreateTime" in data:
        import aws_sdk_controlcatalog.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["CreateTime"]
            )
        )
    else:
        raise DeserializationError("ObjectiveSummary.create_time required")
    if "LastUpdateTime" in data:
        import aws_sdk_controlcatalog.types._prelude.timestamp

        out["last_update_time"] = (
            aws_sdk_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["LastUpdateTime"]
            )
        )
    else:
        raise DeserializationError("ObjectiveSummary.last_update_time required")
    return out
