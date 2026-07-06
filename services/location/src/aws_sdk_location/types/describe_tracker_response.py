"""Generated from Smithy shape ``com.amazonaws.location#DescribeTrackerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.kms_key_id
    import aws_sdk_location.types.position_filtering
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.tag_map
    import aws_sdk_location.types.timestamp


class DescribeTrackerResponse(TypedDict, closed=True):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource.</p>"""
    tracker_arn: "aws_sdk_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:tracker/ExampleTracker</code> </p> </li> </ul>"""
    description: "aws_sdk_location.types.resource_description.ResourceDescription"
    """<p>The optional description for the tracker resource.</p>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>Always returns <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>No longer used. Always returns an empty string.</p>"""
    tags: NotRequired["aws_sdk_location.types.tag_map.TagMap"]
    """<p>The tags associated with the tracker resource.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the tracker resource was created in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    r"""<p>The timestamp for when the tracker resource was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    kms_key_id: NotRequired["aws_sdk_location.types.kms_key_id.KmsKeyId"]
    r"""<p>A key identifier for an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html\">Amazon Web Services KMS customer managed key</a> assigned to the Amazon Location resource.</p>"""
    position_filtering: NotRequired[
        "aws_sdk_location.types.position_filtering.PositionFiltering"
    ]
    """<p>The position filtering method of the tracker resource.</p>"""
    event_bridge_enabled: NotRequired["bool"]
    """<p>Whether <code>UPDATE</code> events from this tracker in EventBridge are enabled. If set to <code>true</code> these events will be sent to EventBridge.</p>"""
    kms_key_enable_geospatial_queries: NotRequired["bool"]
    r"""<p>Enables <code>GeospatialQueries</code> for a tracker that uses a <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html\">Amazon Web Services KMS customer managed key</a>.</p> <p>This parameter is only used if you are using a KMS customer managed key.</p> <note> <p>If you wish to encrypt your data using your own KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your KMS managed key. The exact device position, however; is still encrypted using your managed key.</p> <p>You can choose to opt-in to the Bounding Polygon Quseries feature. This is done by setting the <code>KmsKeyEnableGeospatialQueries</code> parameter to true when creating or updating a Tracker.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTrackerResponse) -> dict:
    out: dict = {}
    out["TrackerName"] = value["tracker_name"]
    out["TrackerArn"] = value["tracker_arn"]
    out["Description"] = value["description"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    if "tags" in value:
        import aws_sdk_location.types.tag_map

        out["Tags"] = aws_sdk_location.types.tag_map.serialize_json(value["tags"])
    import aws_sdk_location.types.timestamp

    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_location.types.timestamp

    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "position_filtering" in value:
        out["PositionFiltering"] = value["position_filtering"]
    if "event_bridge_enabled" in value:
        out["EventBridgeEnabled"] = value["event_bridge_enabled"]
    if "kms_key_enable_geospatial_queries" in value:
        out["KmsKeyEnableGeospatialQueries"] = value[
            "kms_key_enable_geospatial_queries"
        ]
    return out


def deserialize_json(data: dict) -> DescribeTrackerResponse:
    out: DescribeTrackerResponse = {}  # type: ignore[typeddict-item]
    if "TrackerName" in data:
        out["tracker_name"] = data["TrackerName"]
    else:
        raise DeserializationError("DescribeTrackerResponse.tracker_name required")
    if "TrackerArn" in data:
        out["tracker_arn"] = data["TrackerArn"]
    else:
        raise DeserializationError("DescribeTrackerResponse.tracker_arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DescribeTrackerResponse.description required")
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "PricingPlanDataSource" in data:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if "Tags" in data:
        import aws_sdk_location.types.tag_map

        out["tags"] = aws_sdk_location.types.tag_map.deserialize_json(data["Tags"])
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp

        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("DescribeTrackerResponse.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp

        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("DescribeTrackerResponse.update_time required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "PositionFiltering" in data:
        out["position_filtering"] = data["PositionFiltering"]
    if "EventBridgeEnabled" in data:
        out["event_bridge_enabled"] = data["EventBridgeEnabled"]
    if "KmsKeyEnableGeospatialQueries" in data:
        out["kms_key_enable_geospatial_queries"] = data["KmsKeyEnableGeospatialQueries"]
    return out
