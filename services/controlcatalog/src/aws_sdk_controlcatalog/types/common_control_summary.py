"""Generated from Smithy shape ``com.amazonaws.controlcatalog#CommonControlSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_controlcatalog.types.associated_domain_summary
    import aws_sdk_controlcatalog.types.associated_objective_summary
    import aws_sdk_controlcatalog.types.common_control_arn


class CommonControlSummary(TypedDict):
    arn: "aws_sdk_controlcatalog.types.common_control_arn.CommonControlArn"
    """<p>The Amazon Resource Name (ARN) that identifies the common control.</p>"""
    name: "str"
    """<p>The name of the common control.</p>"""
    description: "str"
    """<p>The description of the common control.</p>"""
    domain: (
        "aws_sdk_controlcatalog.types.associated_domain_summary.AssociatedDomainSummary"
    )
    """<p>The domain that the common control belongs to.</p>"""
    objective: "aws_sdk_controlcatalog.types.associated_objective_summary.AssociatedObjectiveSummary"
    """<p>The objective that the common control belongs to.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the common control was created.</p>"""
    last_update_time: "datetime.datetime"
    """<p>The time when the common control was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonControlSummary) -> dict:
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
    import aws_sdk_controlcatalog.types.associated_objective_summary

    out["Objective"] = (
        aws_sdk_controlcatalog.types.associated_objective_summary.serialize_json(
            value["objective"]
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


def deserialize_json(data: dict) -> CommonControlSummary:
    out: CommonControlSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CommonControlSummary.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CommonControlSummary.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CommonControlSummary.description required")
    if "Domain" in data:
        import aws_sdk_controlcatalog.types.associated_domain_summary

        out["domain"] = (
            aws_sdk_controlcatalog.types.associated_domain_summary.deserialize_json(
                data["Domain"]
            )
        )
    else:
        raise DeserializationError("CommonControlSummary.domain required")
    if "Objective" in data:
        import aws_sdk_controlcatalog.types.associated_objective_summary

        out["objective"] = (
            aws_sdk_controlcatalog.types.associated_objective_summary.deserialize_json(
                data["Objective"]
            )
        )
    else:
        raise DeserializationError("CommonControlSummary.objective required")
    if "CreateTime" in data:
        import aws_sdk_controlcatalog.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["CreateTime"]
            )
        )
    else:
        raise DeserializationError("CommonControlSummary.create_time required")
    if "LastUpdateTime" in data:
        import aws_sdk_controlcatalog.types._prelude.timestamp

        out["last_update_time"] = (
            aws_sdk_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["LastUpdateTime"]
            )
        )
    else:
        raise DeserializationError("CommonControlSummary.last_update_time required")
    return out
