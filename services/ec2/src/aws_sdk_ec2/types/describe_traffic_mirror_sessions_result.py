"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrafficMirrorSessionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_mirror_session_set


class DescribeTrafficMirrorSessionsResult(TypedDict, closed=True):
    traffic_mirror_sessions: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_session_set.TrafficMirrorSessionSet"
    ]
    """<p>Describes one or more Traffic Mirror sessions. By default, all Traffic Mirror sessions are described. Alternatively, you can filter the results.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrafficMirrorSessionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_sessions" in value:
        import aws_sdk_ec2.types.traffic_mirror_session_set

        aws_sdk_ec2.types.traffic_mirror_session_set.serialize_ec2_query(
            value["traffic_mirror_sessions"], pairs, f"{prefix}.TrafficMirrorSessionSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrafficMirrorSessionsResult:
    out: DescribeTrafficMirrorSessionsResult = {}  # type: ignore[typeddict-item]
    if el.find("TrafficMirrorSessionSet") is not None:
        import aws_sdk_ec2.types.traffic_mirror_session_set

        out["traffic_mirror_sessions"] = (
            aws_sdk_ec2.types.traffic_mirror_session_set.deserialize_ec2_query(
                el, "TrafficMirrorSessionSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
