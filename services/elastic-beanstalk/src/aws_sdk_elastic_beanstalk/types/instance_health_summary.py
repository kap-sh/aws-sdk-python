"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#InstanceHealthSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.nullable_integer


class InstanceHealthSummary(TypedDict, closed=True):
    no_data: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Grey.</b> AWS Elastic Beanstalk and the health agent are reporting no data on an instance.</p>"""
    unknown: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Grey.</b> AWS Elastic Beanstalk and the health agent are reporting an insufficient amount of data on an instance.</p>"""
    pending: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Grey.</b> An operation is in progress on an instance within the command timeout.</p>"""
    ok: NotRequired["aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"]
    """<p> <b>Green.</b> An instance is passing health checks and the health agent is not reporting any problems.</p>"""
    info: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Green.</b> An operation is in progress on an instance.</p>"""
    warning: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Yellow.</b> The health agent is reporting a moderate number of request failures or other issues for an instance or environment.</p>"""
    degraded: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Red.</b> The health agent is reporting a high number of request failures or other issues for an instance or environment.</p>"""
    severe: NotRequired[
        "aws_sdk_elastic_beanstalk.types.nullable_integer.NullableInteger"
    ]
    """<p> <b>Red.</b> The health agent is reporting a very high number of request failures or other issues for an instance or environment.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceHealthSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "no_data" in value:
        pairs.append((f"{prefix}.NoData", str(value["no_data"])))
    if "unknown" in value:
        pairs.append((f"{prefix}.Unknown", str(value["unknown"])))
    if "pending" in value:
        pairs.append((f"{prefix}.Pending", str(value["pending"])))
    if "ok" in value:
        pairs.append((f"{prefix}.Ok", str(value["ok"])))
    if "info" in value:
        pairs.append((f"{prefix}.Info", str(value["info"])))
    if "warning" in value:
        pairs.append((f"{prefix}.Warning", str(value["warning"])))
    if "degraded" in value:
        pairs.append((f"{prefix}.Degraded", str(value["degraded"])))
    if "severe" in value:
        pairs.append((f"{prefix}.Severe", str(value["severe"])))


def deserialize_query(el: Element) -> InstanceHealthSummary:
    out: InstanceHealthSummary = {}  # type: ignore[typeddict-item]
    child_no_data = el.find("NoData")
    if child_no_data is not None:
        out["no_data"] = int(child_no_data.text or "")
    child_unknown = el.find("Unknown")
    if child_unknown is not None:
        out["unknown"] = int(child_unknown.text or "")
    child_pending = el.find("Pending")
    if child_pending is not None:
        out["pending"] = int(child_pending.text or "")
    child_ok = el.find("Ok")
    if child_ok is not None:
        out["ok"] = int(child_ok.text or "")
    child_info = el.find("Info")
    if child_info is not None:
        out["info"] = int(child_info.text or "")
    child_warning = el.find("Warning")
    if child_warning is not None:
        out["warning"] = int(child_warning.text or "")
    child_degraded = el.find("Degraded")
    if child_degraded is not None:
        out["degraded"] = int(child_degraded.text or "")
    child_severe = el.find("Severe")
    if child_severe is not None:
        out["severe"] = int(child_severe.text or "")
    return out
