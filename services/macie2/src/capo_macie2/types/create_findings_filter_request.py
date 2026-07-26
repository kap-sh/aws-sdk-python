"""Generated from Smithy shape ``com.amazonaws.macie2#CreateFindingsFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer
    import capo_macie2.types.__string
    import capo_macie2.types.finding_criteria
    import capo_macie2.types.findings_filter_action
    import capo_macie2.types.tag_map


class CreateFindingsFilterRequest(TypedDict, closed=True):
    action: NotRequired["capo_macie2.types.findings_filter_action.FindingsFilterAction"]
    """<p>The action to perform on findings that match the filter criteria (findingCriteria). Valid values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, don't perform any action on the findings.</p>"""
    client_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A custom description of the filter. The description can contain as many as 512 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie.</p>"""
    finding_criteria: NotRequired["capo_macie2.types.finding_criteria.FindingCriteria"]
    """<p>The criteria to use to filter findings.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie.</p>"""
    position: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.</p>"""
    tags: NotRequired["capo_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies the tags to associate with the filter.</p> <p>A findings filter can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFindingsFilterRequest) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_macie2.types.findings_filter_action

        out["action"] = capo_macie2.types.findings_filter_action.serialize_json(
            value["action"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "finding_criteria" in value:
        import capo_macie2.types.finding_criteria

        out["findingCriteria"] = capo_macie2.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "position" in value:
        out["position"] = value["position"]
    if "tags" in value:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFindingsFilterRequest:
    out: CreateFindingsFilterRequest = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_macie2.types.findings_filter_action

        out["action"] = capo_macie2.types.findings_filter_action.deserialize_json(
            data["action"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "findingCriteria" in data:
        import capo_macie2.types.finding_criteria

        out["finding_criteria"] = capo_macie2.types.finding_criteria.deserialize_json(
            data["findingCriteria"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "position" in data:
        out["position"] = data["position"]
    if "tags" in data:
        import capo_macie2.types.tag_map

        out["tags"] = capo_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
