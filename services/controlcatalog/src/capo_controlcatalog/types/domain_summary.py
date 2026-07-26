"""Generated from Smithy shape ``com.amazonaws.controlcatalog#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_controlcatalog.types.domain_arn


class DomainSummary(TypedDict, closed=True):
    arn: "capo_controlcatalog.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) that identifies the domain.</p>"""
    name: "str"
    """<p>The name of the domain.</p>"""
    description: "str"
    """<p>The description of the domain.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the domain was created.</p>"""
    last_update_time: "datetime.datetime"
    """<p>The time when the domain was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    import capo_controlcatalog.types._prelude.timestamp

    out["CreateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_controlcatalog.types._prelude.timestamp

    out["LastUpdateTime"] = capo_controlcatalog.types._prelude.timestamp.serialize_json(
        value["last_update_time"]
    )
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DomainSummary.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DomainSummary.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DomainSummary.description required")
    if "CreateTime" in data:
        import capo_controlcatalog.types._prelude.timestamp

        out["create_time"] = (
            capo_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["CreateTime"]
            )
        )
    else:
        raise DeserializationError("DomainSummary.create_time required")
    if "LastUpdateTime" in data:
        import capo_controlcatalog.types._prelude.timestamp

        out["last_update_time"] = (
            capo_controlcatalog.types._prelude.timestamp.deserialize_json(
                data["LastUpdateTime"]
            )
        )
    else:
        raise DeserializationError("DomainSummary.last_update_time required")
    return out
