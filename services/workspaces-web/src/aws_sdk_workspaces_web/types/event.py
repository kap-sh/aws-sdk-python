"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Event``."""

from typing import Literal, TypeAlias, cast

Event: TypeAlias = Literal[
    "WebsiteInteract",
    "FileDownloadFromSecureBrowserToRemoteDisk",
    "FileTransferFromRemoteToLocalDisk",
    "FileTransferFromLocalToRemoteDisk",
    "FileUploadFromRemoteDiskToSecureBrowser",
    "ContentPasteToWebsite",
    "ContentTransferFromLocalToRemoteClipboard",
    "ContentCopyFromWebsite",
    "UrlLoad",
    "TabOpen",
    "TabClose",
    "PrintJobSubmit",
    "SessionConnect",
    "SessionStart",
    "SessionDisconnect",
    "SessionEnd",
    "UrlBlockByContentFilter",
]


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> str:
    return value


def deserialize_json(data: str) -> Event:
    return cast(Event, data)
